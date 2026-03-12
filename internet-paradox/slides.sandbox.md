# LA PARADOJA DE INTERNET

<div class="servers">
  <img src="ServerCabinet.svg" class="server server-aws" alt="AWS">
  <img src="ServerCabinet.svg" class="server server-azure" alt="Azure">
  <img src="ServerCabinet.svg" class="server server-gcp" alt="GCP">
</div>

#### Micro-descentralizada / Macro-centralizada

<small>Jorge Barata</small>
<small>T3chFest 2026</small>

Note:
Presentación: 20 minutos + 10 de preguntas.
Internet nació distribuida, pero hoy depende de unos pocos gigantes.
Bienvenidos a la paradoja.

---

## **Parte 1:** El Colapso

### **Parte 1:** El Colapso

Botón de **emergencia**

Note:
(Minutos 0-3)
Arranque "in media res".

--

### 20 de Octubre de 2025

- **09:00 AM:** Fallo en Bizum.
- **09:15 AM:** App del banco caída.
- **09:30 AM:** Spotify y logística paralizados.

> "Un solo centro de datos en Virginia (AWS) estornudó, y el mundo digital cogió una pulmonía."

Note:
Es la mañana del 20 de octubre de 2025. Bajas a la cafetería, intentas pagar con Bizum y da error.
No es un ciberataque. Es un fallo en un datacenter.

--

### Noviembre de 2025

- ChatGPT caído.
- X (Twitter) inaccesible.
- League of Legends desconectado.

> **Causa:** Un cambio de permisos en un archivo de configuración de **Cloudflare**.

Note:
Apenas un mes después. Esta vez no fue la nube, fue el escudo.
Un simple cambio de permisos tiró abajo la red global.
Dos errores minúsculos. Dos colapsos globales.

---

### Parte 2: El Misterio

#### El mito del Internet indestructible

Note:
(Minutos 3-7)
Vamos a ver cómo hemos llegado aquí.

--

### El Origen: ARPANET & TCP/IP

- Diseño original: **Red distribuida**.
- Objetivo: Sobrevivir a fallos locales.
- Resiliencia a nivel **Micro**.

Note:
Internet se diseñó para que si un nodo caía, el tráfico buscara otro camino.
Esa es la teoría.

--

### La Centralización Invisible

¿Qué tienen en común **Tinder** y **Trello**?

Note:
Pregunta al público: ¿Qué tienen Tinder y Trello en común?
Aparte de que en uno organizas tu trabajo y en el otro tu vida amorosa...

--

### La respuesta está en el DNS

Al resolver sus dominios, la respuesta es idéntica:
**Mismas máquinas, misma infraestructura.**

- `api.gotinder.com` -> Cloudfront (AWS)
- `api.trello.com` -> Cloudfront (AWS)

Note:
Aunque parecen servicios opuestos, viven físicamente en el mismo servidor.
Si cae ese servidor, no puedes trabajar... ni ligar.

---

### Parte 3: La Anatomía

#### Los señores del tráfico

Note:
(Minutos 7-13)
¿Por qué hemos acabado todos en el mismo edificio?

--

### Física y Latencia

- De texto plano -> Vídeo 4K y Tiempo Real.
- La luz tiene velocidad finita.
- **Solución:** Necesitamos servidores _cerca_ de todo el mundo.

Note:
Nos volvimos impacientes.
Como ninguna empresa normal puede pagarse servidores en 100 países, se lo alquilamos a quien sí puede.

--

### El Oligopolio de la Nube

![Gráfico Synergy Research Group](ruta-a-imagen-grafico-nube.jpg)

- **AWS:** ~31%
- **Azure:** ~24%
- **Google Cloud:** ~11%
- **Total:** ~68% del mercado

<small>Fuente: Synergy Research Group / Canalys</small>

Note:
Hemos construido un rascacielos gigantesco sobre un puñado de pilares.
Datos financieros y de infraestructura confirman que 3 empresas controlan 2/3 de la nube.

--

### Los Escudos (CDNs)

![Gráfico W3Techs](ruta-a-imagen-grafico-cdn.jpg)

- **Cloudflare:** ~40% de los sitios web.
- Uso real en producción (W3Techs).

Note:
Si miramos adopción técnica real, Cloudflare gestiona casi la mitad de las webs populares.

--

### Cuando los pilares fallan...

> **EL PAÍS (2021):** "Fastly: cómo una sola empresa ha provocado la caída de internet"

> **LA VANGUARDIA (2021):** "Caída mundial de WhatsApp, Instagram y Facebook"

> **EL MUNDO (2025):** "El 'apagón' global de Cloudflare"

Note:
La hemeroteca lleva años avisando.
No hace falta un misil nuclear. Solo una config mal hecha un martes por la mañana.

---

### Parte 4: El Giro Inesperado

#### Poder, Control y... Fútbol

Note:
(Minutos 13-17)
Aquí es donde la cosa se pone fea a nivel social.

--

### Herramientas para todos

![Gráfico: Hacker y Banco usando misma nube](ruta-a-imagen-tools.jpg)

La misma infraestructura sirve para:

- Bancos 🏦
- Hospitales 🏥
- Phishing masivo 🎣
- Streaming pirata 🏴‍☠️

Note:
Los "malos" usan la misma tecnología que los "buenos".
¿Dónde alojan los piratas sus streamings para que no se caigan? En la nube.

--

### La Nostalgia Pirata

![Decodificador antiguo y tarjeta pirata](ruta-a-imagen-decodificador.jpg)

¿Os acordáis de esto?

Note:
Levantad la mano los que recordéis las tarjetas funcard y el Canal+.
Hoy, el pirata no usa tarjetas, usa Cloudflare para ocultar su IP y tener velocidad.

--

### LaLiga vs. La Nube

- **El problema:** Streaming ilegal detrás de CDNs.
- **La solución:** Bloqueos dinámicos de IPs.
- **El resultado:** Matar moscas a cañonazos. 💣

![Meme cañón contra mosca](ruta-a-imagen-canon.jpg)

Note:
LaLiga consiguió una orden para bloquear IPs dinámicamente.
Pero una IP de Cloudflare no es un servidor, es una puerta para miles de sitios legítimos.
Al bloquear la IP del pirata, bloqueas todo lo demás.

--

### Daño Colateral: hayahora.futbol

![Gráfica hayahora.futbol](ruta-a-imagen-hayahora.jpg)

Las caídas de servicios legítimos coinciden con los horarios de los partidos.

Note:
Esta web monitoriza fallos técnicos.
Las líneas verticales son los partidos. Coinciden perfectamente con caídas de webs de zapatos, servicios personales, etc.
Hemos creado un sistema de censura automatizada.

---

### Conclusión

#### Convivir con la paradoja

- **Micro-descentralizado:** En teoría.
- **Macro-centralizado:** En la práctica.

**El reto para ingenieros:**
Diseñar asumiendo que "la nube" no es mágica, es el ordenador de otro... y ese otro también falla.

Note:
(Minutos 17-20)
Debemos aceptar esta dualidad.
Pasamos a preguntas.

---

### ¡Gracias!

#### Preguntas y Respuestas

[neuralhacker](https://twitter.com/neuralhacker)

Note:
Turno de preguntas (10 minutos).
