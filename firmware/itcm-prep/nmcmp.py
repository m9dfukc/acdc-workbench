import subprocess, sys
NM="/Applications/ArmGNUToolchain/12.2.rel1/arm-none-eabi/bin/arm-none-eabi-nm"
root="/Users/m9dfukc/Desktop/acdc/firmware/builds/"
builds=sys.argv[1:]
def syms(b):
    out=subprocess.run([NM,"-C","-S",root+b+"/ACDC.elf"],capture_output=True,text=True).stdout
    d={}
    for l in out.splitlines():
        p=l.split(" ",3)
        if len(p)==4: a,sz,t,n=p
        else:
            p=l.split(" ",2)
            if len(p)<3: continue
            a,t,n=p; sz="0"
        n=n.split("(")[0] if not n.startswith("USBD_AUDIO_SOF(_USBD") else n
        d.setdefault(n,(int(a,16),int(sz,16),t))
    return d
D={b:syms(b) for b in builds}
want=["SAI1_IRQHandler","DMA1_Stream0_IRQHandler","DMA1_Stream1_IRQHandler","OTG_FS_IRQHandler","HAL_SAI_IRQHandler","HAL_DMA_IRQHandler","SAI_DMATxCplt","SAI_DMATxHalfCplt","HAL_SAI_TxHalfCpltCallback","HAL_SAI_TxCpltCallback","audioCallback","onProgramReady","usbd_rx_convert","usbd_tx_convert","USBD_AUDIO_DataIn","USBD_AUDIO_DataOut","usbd_audio_sof_callback","runAudioTask","onLoop","setLed","programVector","codec","usbd_audio_handle","hUsbDeviceFS","usbd_rx","usbd_tx","codec_txbuf","codec_rxbuf","acdc_raw"]
print("| symbol | "+" | ".join(builds)+" |")
print("|---"*(len(builds)+1)+"|")
ref=D[builds[0]]
for w in want:
    row=[]
    for b in builds:
        v=D[b].get(w)
        if not v: row.append("–"); continue
        s=f"`{v[0]:08x}` ({v[1]})"
        r=ref.get(w)
        if b!=builds[0] and r: 
            dd=v[0]-r[0]; s+=f" Δ{dd:+#x}" if dd else " ="
        row.append(s)
    print(f"| {w} | "+" | ".join(row)+" |")
# global stats: functions with same address
for b in builds[1:]:
    common=[n for n in ref if n in D[b] and ref[n][2] in "Tt" ]
    same=sum(1 for n in common if D[b][n][0]==ref[n][0])
    print(f"\n{b}: text symbols common {len(common)}, same addr {same}")
