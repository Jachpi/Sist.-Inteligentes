def sorcen_dice(usuario_bag, pelicula_bag):
        return 2 * len(usuario_bag.keys() & pelicula_bag.keys())/(len(pelicula_bag.keys())+len(usuario_bag.keys()))




