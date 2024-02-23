distancia = float(input('Digite uma distancia em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
m = distancia
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print('{:.3f} km\n {:.3f} hm\n {:.3f} dam\n {:.3f} m\n {:.0f} dm\n {:.0f} cm\n {:.0f} mm'.format(km, hm, dam, m, dm, cm, mm))

