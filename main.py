import sys
from geocoder import get_coordinates, get_ll_span, get_nearest_object
from mapapi import show_map


def main(toponim):
    ll, spn = get_ll_span(toponim)
    pt0 = ll + ',pmdom1'
    obj_ll = get_nearest_object(ll.split(',', 'аптека'))
    pt = obj_ll + ',pmdom2'
    show_map(f'll={ll}&spn={spn}&pt={pt0}~{pt}')


if __name__ == '__main__':
    t = " ".join(sys.argv[1:])
    t = "Казань,Шамиля-Усманова19"
    if t:
        main(t)