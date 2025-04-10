import discord
from discord.ext import commands
import os
TOKEN = os.getenv('DISCORD_TOKEN')  # ✅ Nueva forma segura

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

# Variables para todos los dioses (puntos iniciales en 0)
dioses = {
    "ZEUS": 0,
    "HERA": 0,
    "POSEIDÓN": 0,
    "DEMETER": 0,
    "ARES": 0,
    "ATENEA": 0,
    "APOLO": 0,
    "ARTEMISA": 0,
    "HEFESTO": 0,
    "AFRODITA": 0,
    "HERMES": 0,
    "DIONISIO": 0,
    "HADES": 0,
    "IRIS": 0,
    "HYPNOS": 0,
    "NÉMESIS": 0,
    "HESTIA": 0,
    "HERACLES": 0,
    "HEBE": 0,
    "HÉCATE": 0,
    "PERSÉFONE": 0,
    "ASCLEPIO": 0,
    "NIKE": 0,
    "TIQUE": 0,
    "JANO": 0,
    "EROS": 0,
    "EOLO": 0,
    "TÁNATOS": 0,
    "FOBOS": 0,
    "DEIMOS": 0,
    "HIGIA": 0,
    "HARMONÍA": 0,
    "ERIS": 0,
    "HEMERA": 0,
    "NIX": 0
}

# Palabras clave para cada dios (completar las que faltan)
palabras_clave = {
    "ZEUS": ["CAPITÁN AMERICA", "THOR", "JULIO VERNE", "GARCÍA MARQUEZ", "BLANCO", "AMARILLO", "AIRE", "ORO", "GRYFINDOR", "THUNDERBIRD", "FACEBOOK", "INSTAGRAM", "PASTAS", "ASADO", "CAFÉ", "VINO", "MONTE RORAIMA", "PLAYA ROJA", "GLADIOLO", "CLAVEL"], #COMPLETO
    "HERA": ["IRON-MAN", "THOR", "JANE AUSTEN", "SHAKESPEARE", "BLANCO", "VIOLETA", "FUEGO", "PLANTA", "GRYFINDOR", "SERPIENTE CORNUDA", "FACEBOOK", "SNAPCHAT", "ENSALADA", "HELADO", "VINO", "TÉ", "MONTE RORAIMA", "CLAVEL", "JACINTO"],  # COMPLETO
    "POSEIDÓN": ["FLASH", "IRON-MAN", "ASIMOV", "VERNE", "AZUL", "VERDE", "AGUA", "GRYFINDOR", "WAMPUS", "INSTAGRAM", "YOUTUBE", "TACOS", "PICADA", "GASEOSA", "CERVEZA", "ISLA MARIETA","CEBU", "JACINTO", "GLADIOLO"],  # COMPLETO
    "DEMETER": ["CAPITÁN AMÉRICA", "WONDER WOMAN", "SHAKESPEARE", "GARCÍA MARQUEZ","MARRON" "VERDE", "TIERRA", "MADERA", "HUFFLEPUFF", "WAMPUS", "PINTEREST", "BLOGGER", "ASADO", "TACOS", "JUGO", "AGUA", "BOSQUE DE BAMBU", "PARQUE", "PARQUE KEUKENHOF", "DELFINIO", "ASTER"],  # COMPLETO
    "ARES": ["SUPERMAN", "THOR", "ASIMOV", "EDGARD A POE", "POE", "NEGRO", "ROJO", "FUEGO", "ORO", "GRYFINDOR", "SERPIENTE CORNUDA", "INSTAGRAM", "YOUTUBE", "PIZZA Y EMPANADAS", "HAMBURGUESAS CON PAPAS", "CAFÉ", "CERVEZA", "PLAYA ROJA", "CEBU", "CLAVEL", "GLADIOLO"],  # COMPLETO
    "ATENEA": ["WONDER WOMAN", "DR STRANGE", "ARTHUR C DOYLE", "ASIMOV", "BLANCO", "AZUL", "AGUA", "ORO", "RAVENCLAW", "THUNDERBIRD", "TWITTER", "BLOGGER", "PASTAS", "HELADO", "CAFÉ", "TÉ", "BOSQUE DE BAMBU", "BOSQUE NEGRO", "MARGARITA", "IRIS"],  # COMPLETO,
    "APOLO": ["SUPERMAN", "CAPITÁN AMERICA","J K ROWLING", "JULIO VERNE", "VERNE", "BLANCO", "AMARILLO", "FUEGO", "ORO", "HUFFLEPUFF", "SERPIENTE CORNUDA", "INSTAGRAM", "SNAPCHAT", "TACOS", "HAMBURGUESA CON PAPAS", "GASEOSA", "CHOCOLATE CALIENTE", "MONTE RIORAMA", "PLAYA ROJA", "AMARILIS", "CLAVEL"],  # COMPLETO,
    "ARTEMISA": ["WONDER WOMAN", "FLASH","JULIO VERNE", "SHAKESPEARE", "NEGRO", "AZUL", "AGUA", "PLATA", "RAVENCLAW", "WAMPUS", "TWITTER", "INSTAGRAM", "ENSALADA", "PANQUEQUES", "JUGO", "AGUA", "BOSQUE NEGRO", "CEBU", "MARGARITA", "ÁSTER"],  # COMPLETO,
    "HEFESTO": ["BATMAN", "FLASH", "JULIO VERNE", "ASIMOV", "NARANJA", "MARRON", "FUEGO", "BRONCE", "RAVENCLAW", "WAMPUS", "PINTEREST", "YOUTUBE", "PIZZA Y EMPANADAS", "TACOS", "CAFÉ", "CERVEZA","MONTE RIORAMA", "MINA DE NAICA", "CLAVEL", "GLADIOLO"],  # COMPLETO,
    "AFRODITA": ["WONDER WOMAN", "IRON-MAN", "JANE AUSTEN", "SHAKSPEARE", "ROJO", "VIOLETA", "FUEGO", "ORO", "SLYTHERIN", "THUNDERBIRD", "FACEBOOK", "INSTAGRAM", "ENSALADA", "MOUSSE DE CHOCOLATE","VINO", "TÉ", "PARQUE KEUKENHOF", "PLAYA ROJA", "AMARILIS", "IRIS"],  # COMPLETO,
    "HERMES": ["FLASH", "DR STRANGE", "JULIO VERNE", "GARCÍA MARQUEZ", "AMARILLO", "VERDE", "AIRE","MADERA", "HUFFLEPUFF", "WAMPUS", "TWITTER", "SNAPCHAT", "TACOS", "HAMBURGUESA CON PAPAS", "GASEOSA", "AGUA", "MONTE RIORAMA", "CEBU", "CLAVEL", "JACINTO"],  # COMPLETO,
    "DIONISIO": ["IRON-MAN", "THOR", "EDGARD A POE", "POE", "GARCIA MARQUEZ","ROJO", "VIOLETA", "TIERRA", "MADERA", "HUFFELPURFF", "SERPIENTE CORNUDA", "FACEBOOK", "INSTAGRAM", "ASADO", "PICADA", "GASEOSA", "VINO", "PLAYA ROJA", "CEBU", "DELFINIO", "GLADIOLO"],  # COMPLETO,
    "HADES": ["BATMAN" + "DR STRANGE" + "EDGARD A POE" + "ARTHUR C DOYLE" + "NEGRO" + "AZUL" + "TIERRA" + "ORO" + "SLYTHERIN" + "SERPIENTE CORNUDA" + "TUMBLR" + "INSTAGRAM" + "PICADA" + "PASTAS" + "CAFÉ C/S LECHE" + "VINO" + "MINA DE NAICA" + "BOSQUE NEGRO" + "IRIS" + "GLADIOLO"],  # COMPLETO,
    "IRIS": ["FLASH" + "J K ROWLING" + "JANE AUSTEN" + "VIOLETA" + "BLANCO" +
    "AGUA" + "BRONCE" + "PUKWUDGIE" + "HUFFLEPUFF" + "INSTAGRAM" +
    "PINTEREST" + "PANQUEQUES" + "MOUSSE DE CHOCOLATE" + "AGUA" +
    "JUGO" + "PARQUE KEUKENHOF" + "PLAYA ROJA" + "GLADIOLO" + "IRIS"],  # Completar,
    "HYPNOS": ["BATMAN" + "IRON-MAN" + "ARTHUR C DOYLE" + "GARCÍA MARQUEZ" + "BLANCO" +
    "NEGRO" + "AGUA" + "AIRE" + "HUFFLEPUFF" + "PUKWUDGIE" +
    "TWITTER" + "PINTEREST" + "HELADO" + "PIZZA Y EMPANADAS" +
    "CHOCOLATE CALIENTE" + "TÉ" + "MONTE RORAIMA" + "CEBU" +
    "MARGARITA" + "ÁSTER"],  # COMPLETO,
    "NÉMESIS": ["BATMAN", "DR STRANGE", "ARTHUR C DOYLE", "W SHAKESPEARE", "BLANCO", "NEGRO", "AGUA", "FUEGO", "SLYTHERIN", "THUNDERBIRD", "TUMBLR", "FACEBOOK", "PIZZA Y EMPANADAS", "HELADO", "CAFÉ C/S LECHE", "VINO", "ISLA MARIETA", "BOSQUE NEGRO", "GLADIOLO", "CLAVEL"],
    "HESTIA": ["WONDER WOMAN", "FLASH", "JANE AUSTEN", "J K ROWLING", "BLANCO", "NARANJA", "FUEGO", "ORO", "HUFFLEPUFF", "WAMPUS", "FACEBOOK", "TUMBLR", "HELADO", "PANQUEQUES", "JUGO", "CHOCOLATE CALIENTE", "PARQUE KEUKENHOF", "SAGANO BOSQUE DE BAMBU", "MARGARITA", "ÁSTER"],
    "HERACLES": ["SUPERMAN", "CAPITAN AMÉRICA", "ARTHUR C DOYLE", "JULIO VERNE", "BLANCO", "MARRON", "FUEGO", "ORO", "GRYFFINDOR", "THUNDERBIRD", "FACEBOOK", "INSTAGRAM", "ASADO", "PICADA", "GASEOSA", "CERVEZA", "MONTE RORAIMA", "ISLA MARIETA", "CLAVEL", "JACINTO"],
    "HEBE": ["WONDER WOMAN", "CAPITAN AMÉRICA", "JANE AUSTEN", "JULIO VERNE", "BLANCO", "AMARILLO", "AGUA", "ORO", "HUFFLEPUFF", "PUKWUDGIE", "YOUTUBE", "BLOGGER", "ENSALADA", "MOUSSE DE CHOCOLATE", "TÉ", "VINO", "PARQUE KEUKENHOF", "SAGANO BOSQUE DE BAMBU", "AMARILIS", "ÁSTER"],
    "HÉCATE": ["WONDER WOMAN", "DR STRANGE", "STEPHEN KING", "J K ROWLING", "VIOLETA", "NEGRO", "BRONCE", "ORO", "RAVENCLAW", "THUNDERBIRD", "INSTAGRAM", "TUMBLR", "SUSHI", "ENSALADA", "CAFÉ C/S LECHE", "JUGO", "BOSQUE NEGRO", "PLAYA ROJA", "IRIS", "GLADIOLO"],
    "PERSÉFONE": ["WONDER WOMAN", "BATMAN", "JANE AUSTEN", "J K ROWLING", "VERDE", "NARANJA", "AGUA", "BRONCE", "WAMPUS", "HUFFLEPUFF", "INSTAGRAM", "PINTEREST", "PANQUEQUES", "ASADO", "VINO", "CAFÉ C/S LECHE", "PLAYA ROJA", "PARQUE KEUKENHOF", "AMARILIS", "CLAVEL"],
    "ASCLEPIO": ["DR STRANGE", "IRON-MAN", "J K ROWLING", "W SHAKESPEARE", "BLANCO", "NEGRO", "AGUA", "AIRE", "RAVENCLAW", "PUKWUDGIE", "TUMBLR", "BLOGGER", "ENSALADA", "SUSHI", "CAFÉ C/S LECHE", "TÉ", "SAGANO BOSQUE DE BAMBU", "PARQUE KEUKENHOF", "IRIS", "ÁSTER"],
    "NIKE": ["WONDER WOMAN", "CAPITAN AMÉRICA", "ARTHUR C DOYLE", "JULIO VERNE", "BLANCO", "VERDE", "FUEGO", "ORO", "GRYFFINDOR", "THUNDERBIRD", "FACEBOOK", "INSTAGRAM", "ASADO", "HELADO", "CAFÉ C/S LECHE", "CERVEZA", "CLAVEL", "GLADIOLO", "MARGARITA", "CLAVEL"],
    "TIQUE": ["WONDER WOMAN", "SPIDERMAN", "STEPHEN KING", "ARTHUR C DOYLE", "VIOLETA", "NEGRO", "TIERRA", "AIRE", "RAVENCLAW", "INSTAGRAM", "TWITTER", "TUMBLR", "PIZZA Y EMPANADAS", "SUSHI", "MOUSSE DE CHOCOLATE", "GASEOSA", "PARQUE KEUKENHOF", "PLAYA ROJA", "IRIS", "ÁSTER"],
    "JANO": ["BATMAN", "SUPERMAN", "STEPHEN KING", "W SHAKESPEARE", "BLANCO", "NEGRO", "AGUA", "FUEGO", "GRYFFINDOR", "TWITTER", "YOUTUBE", "INSTAGRAM", "SUSHI", "HELADO", "GASEOSA", "TÉ", "PLAYA ROJA", "ISLA MARIETA", "IRIS", "ÁSTER"],
    "EROS": ["IRON-MAN", "BATMAN", "JANE AUSTEN", "W SHAKESPEARE", "NEGRO", "ROJO", "FUEGO", "ORO", "GRYFFINDOR", "THUNDERBIRD", "TWITTER", "INSTAGRAM", "SUSHI", "PANQUEQUES", "GASEOSA", "TÉ", "ISLA MARIETA", "PLAYA ROJA", "IRIS", "CLAVEL"],
    "EOLO": ["FLASH", "SPIDERMAN", "STEPHEN KING", "J K ROWLING", "BLANCO", "AZUL", "TIERRA", "ORO", "RAVENCLAW", "THUNDERBIRD", "TWITTER", "FACEBOOK", "PIZZA Y EMPANADAS", "SUSHI", "MOUSSE DE CHOCOLATE", "GASEOSA", "PARQUE KEUKENHOF", "PLAYA ROJA", "IRIS", "ÁSTER"],
    "TÁNATOS": ["BATMAN", "DR STRANGE", "EDGARD A POE", "W SHAKESPEARE", "NEGRO", "AZUL", "MADERA", "TIERRA", "SLYTHERIN", "SERPIENTE CORNUDA", "TUMBLR", "FACEBOOK", "PIZZA Y EMPANADAS", "SUSHI", "GASEOSA", "CAFÉ C/S LECHE", "MONTE RORAIMA", "BOSQUE NEGRO", "MARGARITA", "JACINTO"],
    "FOBOS": ["BATMAN", "SPIDERMAN", "EDGARD A POE", "ARTHUR C DOYLE", "NEGRO", "VIOLETA", "TIERRA", "AIRE", "GRYFFINDOR", "THUNDERBIRD", "TUMBLR", "FACEBOOK", "ENSALADA", "SUSHI", "GASEOSA", "TÉ", "MONTE RORAIMA", "BOSQUE NEGRO", "AMARILIS", "CLAVEL"],
    "DEIMOS": ["BATMAN", "CAPITAN AMÉRICA", "EDGARD A POE", "GARCÍA MARQUEZ", "NEGRO", "ROJO", "TIERRA", "AGUA", "SERPIENTE CORNUDA", "WAMPUS", "YOUTUBE", "BLOGGER", "PICADA", "MOUSSE DE CHOCOLATE", "VINO", "CERVEZA", "ISLA MARIETA", "SAGANO BOSQUE DE BAMBU", "IRIS", "JACINTO"],
    "HIGIA": ["DR STRANGE", "FLASH", "JANE AUSTEN", "W SHAKESPEARE", "BLANCO", "AZUL", "AGUA", "ORO", "HUFFLEPUFF", "PUKWUDGIE", "YOUTUBE", "BLOGGER", "ENSALADA", "SUSHI", "TÉ", "VINO", "BOSQUE NEGRO", "PLAYA ROJA", "MARGARITA", "ÁSTER"],
    "HARMONÍA": ["DR STRANGE", "FLASH", "JANE AUSTEN", "J K ROWLING", "BLANCO", "AZUL", "AGUA", "ORO", "RAVENCLAW", "PUKWUDGIE", "TUMBLR", "FACEBOOK", "ENSALADA", "PANQUEQUES", "TÉ", "CAFÉ C/S LECHE", "BOSQUE NEGRO", "SAGANO BOSQUE DE BAMBU", "AMARILIS", "CLAVEL"],
    "ERIS": ["SUPERMAN", "CAPITAN AMÉRICA", "JANE AUSTEN", "GARCÍA MARQUEZ", "BLANCO", "AMARILLO", "TIERRA", "AIRE", "RAVENCLAW", "WAMPUS", "FACEBOOK", "BLOGGER", "SUSHI", "HELADO", "GASEOSA", "VINO", "MONTE RORAIMA", "SAGANO BOSQUE DE BAMBU", "AMARILIS", "ÁSTER"],
    "HEMERA": ["WONDER WOMAN", "SUPERMAN", "JANE AUSTEN", "J K ROWLING", "AMARILLO", "NARANJA", "AGUA", "ORO", "RAVENCLAW", "WAMPUS", "YOUTUBE", "FACEBOOK", "ENSALADA", "HELADO", "GASEOSA", "CERVEZA", "PARQUE KEUKENHOF", "MONTE RORAIMA", "AMARILIS", "ÁSTER"],
    "NIX": ["BATMAN", "FLASH", "EDGARD A POE", "STEPHEN KING", "NEGRO", "VIOLETA", "MADERA", "PLATA", "GRYFFINDOR", "PUKWUDGIE", "TWITTER", "FACEBOOK", "PIZZA Y EMPANADAS", "SUSHI", "GASEOSA", "TÉ", "MONTE RORAIMA", "BOSQUE NEGRO", "MARGARITA", "ÁSTER"]

}

# Descripciones para cada dios (completar las que faltan)
descripciones = {
    "ZEUS": "EL MAS CAPO", # Completar
    "HERA": "LA MAS CAPA",  # Completar
    "POSEIDÓN": "",  # Completar
    # ... completar para los demás dioses
}

@bot.command()
async def test(ctx, *, respuestas: str):
    # Mensaje inicial con mención
    await ctx.send(f"{ctx.author.mention} 🔍 Analizando tus respuestas...")

    # Reiniciar puntos (conserva tu lógica)
    for dios in dioses:
        dioses[dios] = 0
    
    # Procesar respuestas (igual que antes)
    palabras_usuario = [p.upper().strip() for p in respuestas.split(',')]
    
    # Contar puntos (usando tu diccionario palabras_clave)
    for palabra in palabras_usuario:
        for dios, palabras in palabras_clave.items():
            if palabra in palabras:
                dioses[dios] += 1
    
    # Ordenar resultados
    resultados_ordenados = sorted(dioses.items(), key=lambda x: x[1], reverse=True)
    
    # Crear Embed (conserva tu estilo)
    embed = discord.Embed(
        title="🏛️ Resultados del Test de DemigodsArg 🏛️",
        description=f"**Usuario:** {ctx.author.mention}",
        color=discord.Color.gold()
    )
    
    # Top 3 dioses
    for i, (dios, puntos) in enumerate(resultados_ordenados[:3], 1):
        embed.add_field(
            name=f"{i}. {dios}",
            value=f"Puntos: {puntos}",
            inline=False
        )
    
    # Dios principal (con mención en el valor)
    dios_principal = resultados_ordenados[0][0]
    embed.add_field(
        name="¡Tu parentesco divino!",
        value=f"**{ctx.author.mention} es hijo de {dios_principal}**\n\n{descripciones.get(dios_principal, '')}",
        inline=False
    )
    
    await ctx.send(embed=embed)
    
@bot.command()
async def ayudatest(ctx):
    """Explica cómo usar el test"""
    ayuda = """
    **Cómo tomar el test:**
    Usa el comando `%test` seguido de tus 10 respuestas separadas por comas.
    
    Ejemplo:
    `%test CAPITÁN AMERICA, THOR, ROSA, MAR, LUNA, ARCO, VINO, MÚSICA, SOL, GUERRA`
    
    El bot analizará tus respuestas y determinará a qué dios griego perteneces.
    """
    await ctx.send(ayuda)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

