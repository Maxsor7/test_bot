import discord
from discord.ext import commands
import secrets_1

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
    "AFRODITA": [],  # Completar,
    "HERMES": [],  # Completar,
    "DIONISIO": [],  # Completar,
    "HADES": [],  # Completar,
    "IRIS": [],  # Completar,
    "HYPNOS": [],  # Completar,
    "NÉMESIS": [],  # Completar,
    "HESTIA": [],  # Completar,
    "HERACLES": [],  # Completar,
    "HEBE": [],  # Completar,
    "HÉCATE": [],  # Completar,
    "PERSÉFONE": [],  # Completar,
    "ASCLEPIO": [],  # Completar,
    "NIKE": [],  # Completar,
    "TIQUE": [],  # Completar,
    "JANO": [],  # Completar,
    "EROS": [],  # Completar,
    "EOLO": [],  # Completar,
    "TÁNATOS": [],  # Completar,
    "FOBOS": [],  # Completar,
    "DEIMOS": [],  # Completar,
    "HIGIA": [],  # Completar,
    "HARMONÍA": [],  # Completar,
    "ERIS": [],  # Completar,
    "HEMERA": [],  # Completar,
    "NIX": []  # Completar
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

bot.run(secrets_1.TOKEN)