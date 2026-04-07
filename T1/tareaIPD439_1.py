import matplotlib.pyplot as plt

sizes = [32, 64, 128, 256, 512, 1024]
sram_memcpy = [2.833, 4.958, 9.0, 17.0, 32.958, 65.0]
sram_dma    = [7.167, 9.333, 13.583, 22.125, 39.167, 73.375]
flash_memcpy = [3.667, 6.25, 11.458, 21.833, 42.625, 84.208]
flash_dma    = [8.542, 12.167, 19.333, 33.75, 62.5, 120.125]

#Grafico origen SRAM:
plt.figure(figsize=(8, 5))
plt.plot(sizes, sram_memcpy, marker='o', linestyle='-', color='tab:blue', label='SRAM -> SRAM (memcpy)')
plt.plot(sizes, sram_dma, marker='s', linestyle='-', color='tab:orange', label='SRAM -> SRAM (DMA)')

plt.title('Tiempos de Transferencia: Origen SRAM', fontsize=14)
plt.xlabel('Tamaño de transferencia [Bytes]', fontsize=12)
plt.ylabel('Tiempo [$\\mu$s]', fontsize=12)

# Escala log para eje X
plt.xscale('log', base=2)
plt.xticks(sizes, sizes) 

plt.grid(True, which="both", ls="--", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig('grafico_sram.png', dpi=300)
plt.show()

#Grafico origen Flash
plt.figure(figsize=(8, 5))
plt.plot(sizes, flash_memcpy, marker='o', linestyle='-', color='tab:blue', label='Flash -> SRAM (memcpy)')
plt.plot(sizes, flash_dma, marker='s', linestyle='-', color='tab:orange', label='Flash -> SRAM (DMA)')

plt.title('Tiempos de Transferencia: Origen Flash', fontsize=14)
plt.xlabel('Tamaño de transferencia [Bytes]', fontsize=12)
plt.ylabel('Tiempo [$\\mu$s]', fontsize=12)

# Escala log para eje X
plt.xscale('log', base=2)
plt.xticks(sizes, sizes)

plt.grid(True, which="both", ls="--", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig('grafico_flash.png', dpi=300)
plt.show()
