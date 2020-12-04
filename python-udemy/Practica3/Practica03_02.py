base=2

caballero   ={'vida':base, 'ataque':base,'defensa':base, 'alcance':base}
guerrero    ={'vida':base, 'ataque':base,'defensa':base, 'alcance':base}
arquero     ={'vida':base, 'ataque':base,'defensa':base, 'alcance':base}

print(f"|caballero\t->\t|vida: {caballero['vida']}\t|ataque: {caballero['ataque']}\t|defensa: {caballero['defensa']}\t|alcance: {caballero['alcance']}")
print(f"|guerrero\t->\t|vida: {guerrero['vida']}\t|ataque: {guerrero['ataque']}\t|defensa: {guerrero['defensa']}\t|alcance: {guerrero['alcance']}")
print(f"|arquero\t->\t|vida: {arquero['vida']}\t|ataque: {arquero['ataque']}\t|defensa: {arquero['defensa']}\t|alcance: {arquero['alcance']}")

print("\n")

caballero['vida']       = guerrero['vida'] * 2
caballero['defensa']    = guerrero['defensa'] * 2

guerrero['ataque']      = caballero['ataque']*2
guerrero['alcance']     = caballero['alcance']*2

arquero['vida']         = guerrero['vida']
arquero['ataque']       = guerrero['alcance']
arquero['defensa']      =int(guerrero['defensa']/2)
arquero['alcance']      = guerrero['alcance']*2


print(f"|caballero\t->\t|vida: {caballero['vida']}\t|ataque: {caballero['ataque']}\t|defensa: {caballero['defensa']}\t|alcance: {caballero['alcance']}")
print(f"|guerrero\t->\t|vida: {guerrero['vida']}\t|ataque: {guerrero['ataque']}\t|defensa: {guerrero['defensa']}\t|alcance: {guerrero['alcance']}")
print(f"|arquero\t->\t|vida: {arquero['vida']}\t|ataque: {arquero['ataque']}\t|defensa: {arquero['defensa']}\t|alcance: {arquero['alcance']}")

c = {1,2,2,3,3,3}
print( list(c) )