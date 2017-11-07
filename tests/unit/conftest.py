# -*- coding: utf-8 -*-
import mock
import pytest
import requests

import bs4

from meneadata.page.meneo import Meneo
from meneadata.page.page import Page

PAGE = """
<!DOCTYPE html>
<html lang="es" prefix="og: http://ogp.me/ns#">
<head>
    <meta charset="utf-8"/>
    <meta name="ROBOTS" content="NOARCHIVE"/>
    <meta name="generator" content="meneame"/>
    <meta name="referrer" content="always">
</head>
<body>
<div class="header-top-wrapper pinned" style="">
    <div id="header-top" class="mnm-center-in-wrap"><a href="/" title="portada Menéame" id="header-logo"
                                                       class="logo-mnm"> <img src="/img/mnm/logo-white.svg"
                                                                              alt="Logo Menéame" height="30"
                                                                              onerror="this.onerror = null; this.src = '/img/mnm/logo-white.png'"/>
    </a> <a href="/m/mnm" class="sub-name wideonly">EDICIóN GENERAL</a>
        <ul id="userinfo">
            <li class="search">
                <div><a id="searchform_button"><i class="fa fa-search"></i></a>
                    <div id="searchform" class="searchform" style="display:none;">
                        <form action="/search" method="get" name="top_search"><input class="searchbox" name="q"
                                                                                     type="search"/></form>
                    </div>
                </div>
            </li>
            <li class="usertext"><a href="/login?return=%2F%3Fpage%3D7060">login</a></li>
            <li class="usertext"><a href="/register">registrarse</a></li>
        </ul>
    </div>
</div>
<div id="header">
    <div class="header-menu-wrapper">
        <div id="header-menu" class="mnm-center-in-wrap">
            <div class="header-menu01">
                <ul class="menu01-itemsl">
                    <li title="enviar nueva historia"><a href="/submit" class="submit_new_post">publicar</a></li>
                    <li title="enviar nueva historia"><a href="/submit?type=article&write=true"
                                                         class="submit_new_article">Crear artículo</a></li>
                    <li title="menear noticias pendientes"><a href="/queue">nuevas</a></li>
                    <li title="Artículos"><a href="/articles" class="button-new">artículos</a> <span class="button-new">nuevo</span>
                    </li>
                    <li title="Subs"><a href="/subs">subs</a></li>
                    <li title="historias más votadas"><a href="/popular">populares</a></li>
                    <li title="historias más visitadas/leídas"><a href="/top_visited">más visitadas</a></li>
                </ul>
                <div class="dropdown menu-more"><a href="#" class="dropdown-toggle menu-more-button" type="button"
                                                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">MÁS
                    <i class="fa fa-angle-down"></i> </a>
                    <ul class="dropdown-menu menu-subheader">
                        <li class="selected"><a href="/">todas</a></li>
                        <li><a href="/m/actualidad">actualidad</a></li>
                        <li><a href="/m/cultura">cultura</a></li>
                        <li><a href="/m/ocio">ocio</a></li>
                        <li><a href="/m/tecnología">tecnología</a></li>
                        <li><a href="/?meta=_*">m/*</a></li>
                        <li class="icon wideonly"><a href="/rss" title=""> <i class="fa fa-rss-square"></i> RSS </a>
                        </li>
                    </ul>
                </div>
                <ul class="menu01-itemsr">
                    <li title="visualizador en tiempo real"><a href="/sneak">fisgona</a></li>
                    <li title="leer o escribir notas y mensajes privados"><a href="/notame/">nótame</a></li>
                    <li><a href="http://meneame.wikispaces.com/Comenzando" title="ayuda para principiantes">Ayuda</a>
                    </li>
                </ul>
            </div>
        </div><!--header-menu01--> </div><!--header-menu-wrapper-->  </div><!--header-->
<div id="variable">
    <div id="wrap">
        <div id="container">
            <div id="sidebar">
                <div class="sidebox brown">
                    <div>
                        <div class="header"><h4><a href="/subs">En subs</a></h4></div>
                        <div class="body">
                            <div class="cell">
                                <div class="votes"><span>4</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856237.jpeg?1509995947"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/ciencia">ciencia</a>&nbsp; <a
                                    href="https://www.meneame.net/story/mamiferos-pasaron-actividad-diurna-despues-extincion-dinosaurios"
                                    class="tooltip l:2856237">Los mamíferos pasaron a la actividad diurna después de la
                                extinción de los dinosaurios (ENG)</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>6</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856250.jpeg?1510019166"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/gilipolleces">gilipolleces</a>&nbsp; <a
                                    href="https://www.meneame.net/story/amarra-hijo-nueve-anos-techo-coche-sujete-piscina"
                                    class="tooltip l:2856250">Amarra a su hijo de nueve años al techo de su coche para
                                que sujete una piscina</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>5</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855535.jpeg?1510042803"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/astronomia">astronomia</a>&nbsp; <a
                                    href="https://www.meneame.net/story/jupiter-pudo-empezar-como-mundo-agua-evaporada"
                                    class="tooltip l:2855535">Júpiter pudo empezar como un mundo de agua evaporada</a>
                            </h5></div>
                            <div class="cell">
                                <div class="votes queued"><span>16</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856301.jpeg?1510006086"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/gilipolleces">gilipolleces</a>&nbsp; <a
                                    href="https://www.meneame.net/story/youtubers-financiados-gobierno-neerlandes-drogan-delante-camara"
                                    class="tooltip l:2856301">Los youtubers financiados por el gobierno neerlandés que
                                se drogan delante de la cámara</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>7</span></div>
                                <h5><a class="subname big" href="/m/Animales">Animales</a>&nbsp; <a
                                        href="https://www.meneame.net/story/capturan-murcielago-casi-dos-metros-envergadura"
                                        class="tooltip l:2856295">Capturan un murciélago de casi dos metros de
                                    envergadura</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>7</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855503.jpeg?1509999902"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/Retuit">Retuit</a>&nbsp; <a
                                    href="https://www.meneame.net/story/conejos-asesinos-miniaturas-medievales"
                                    class="tooltip l:2855503">Conejos asesinos en las miniaturas medievales</a></h5>
                            </div>
                            <div class="cell">
                                <div class="votes queued"><span>34</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/93/media_thumb-link-2855892.jpeg?1509960907"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/Sucesos">Sucesos</a>&nbsp; <a
                                    href="https://www.meneame.net/story/mujer-mata-esposo-cuatros-hijos"
                                    class="tooltip l:2855892">Mujer mata a su esposo y a sus cuatros hijos</a></h5>
                            </div>
                            <div class="cell">
                                <div class="votes queued"><span>17</span></div>
                                <h5><a class="subname big" href="/m/ciencia">ciencia</a>&nbsp; <a
                                        href="https://www.meneame.net/story/primer-numero-nature-online-148-aniversario-revista"
                                        class="tooltip l:2855190">Primer número de Nature online en el 148 aniversario
                                    de la revista</a></h5></div>
                            <div class="cell">
                                <div class="votes queued"><span>50</span></div>
                                <h5><a class="subname big" href="/m/Artículos">Artículos</a>&nbsp; <a
                                        href="https://www.meneame.net/story/reto-30-cuentos-6-muerto-encargo"
                                        class="tooltip l:2856188">El reto de los 30 cuentos. 6.- Muerto por encargo</a>
                                </h5></div>
                            <div class="cell">
                                <div class="votes"><span>10</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855601.jpeg?1509911767"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="En subs" class="thumbnail lazy"/>  <h5>
                                <a class="subname big" href="/m/Cine">Cine</a>&nbsp; <a
                                    href="https://www.meneame.net/story/8-terrorificos-remakes-superaron-pelicula-original"
                                    class="tooltip l:2855601">8 terroríficos remakes que superaron a la película
                                original</a></h5></div>
                        </div>
                    </div>
                </div>
                <div class="sidebox-rounded orange">
                    <div class="header"><h4><a href="https://www.meneame.net/m/Pregúntame">PREGÚNTAME</a></h4></div>
                    <div class="body">
                        <div class="finished">FINALIZADOS</div>
                        <div class="guest"><a title="Santi García Cremades "
                                              href="https://www.meneame.net/m/Preg%C3%BAntame/hola-soy-santi-garcia-cremades-matematico-divulgador-cientifico">
                            <img alt="Santi García Cremades "
                                 src="https://www.meneame.net/backend/media?type=preguntame&amp;id=5&amp;version=0&amp;ts=1508855013&amp;image.jpeg"/>
                            <div class="guest-name">Santi García Cremades</div>
                            <div class="guest-description">Matemático, divulgador científico y mejor persona</div>
                            <span class="show-responses"> Ver respuestas &raquo;  </span> </a></div>
                        <div class="guest"><a title="Javier Arranz"
                                              href="https://www.meneame.net/m/Preg%C3%BAntame/hola-soy-javier-arranz-ocu-preguntame/">
                            <img alt="Javier Arranz"
                                 src="https://www.meneame.net/backend/media?type=preguntame&amp;id=4&amp;version=0&amp;ts=1506335471&amp;image.png"/>
                            <div class="guest-name">Javier Arranz</div>
                            <div class="guest-description">Experto de OCU en materia energética</div>
                            <span class="show-responses"> Ver respuestas &raquo;  <span
                                    class="sponsored">patrocinado</span>  </span> </a></div>
                        <div class="guest"><a title="Beatriz Hervella Nogueira"
                                              href="https://www.meneame.net/m/Preg%C3%BAntame/hola-soy-bea-hervella-meteorologa-preguntame">
                            <img alt="Beatriz Hervella Nogueira"
                                 src="https://www.meneame.net/backend/media?type=preguntame&amp;id=1&amp;version=0&amp;ts=1502119518&amp;image.jpeg"/>
                            <div class="guest-name">Beatriz Hervella Nogueira</div>
                            <div class="guest-description">Meteoróloga</div>
                            <span class="show-responses"> Ver respuestas &raquo;  </span> </a></div>
                        <div class="guest"><a title="Marián García"
                                              href="https://www.meneame.net/m/Preg%C3%BAntame/hola-soy-marian-garcia-dra-farmacia-nutricionista-divulgadora">
                            <img alt="Marián García"
                                 src="https://www.meneame.net/backend/media?type=preguntame&amp;id=2&amp;version=0&amp;ts=1502119779&amp;image.jpeg"/>
                            <div class="guest-name">Marián García</div>
                            <div class="guest-description">Dra. Farmacia, nutricionista y divulgadora sanitaria.</div>
                            <span class="show-responses"> Ver respuestas &raquo;  </span> </a></div>
                    </div>
                </div>
                <div class="sidebox red">
                    <div>
                        <div class="header"><h4><a href="/top_active">destacadas</a></h4></div>
                        <div class="body">
                            <div class="cell">
                                <div class="votes"><span>293</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856373.jpeg?1510019466"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="destacadas" class="thumbnail lazy"/><h5>
                                <a href="/story/padre-homofobo-mata-hijo-gay-14-anos" class="tooltip l:2856373">Un padre
                                    homófobo mata a su hijo gay de 14 años</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>155</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/93/media_thumb-link-2855774.jpeg?1509913866"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="destacadas" class="thumbnail lazy"/><h5>
                                <a href="/story/10-fenomenos-naturales-mas-extranos-existen-merecen-ser-visto"
                                   class="tooltip l:2855774">10 de los fenómenos naturales más extraños que existen y
                                    que merecen ser visto al menos una vez en la vida</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>555</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856362.jpeg?1510012806"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="destacadas" class="thumbnail lazy"/><h5>
                                <a href="/story/exito-mundial-proyecto-captura-co2-hizo-islandia-tras-abandono"
                                   class="tooltip l:2856362">Éxito mundial de proyecto de captura de CO2 que sí se hizo
                                    en Islandia tras el abandono institucional del de España</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>132</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856305.jpeg?1510001466"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="destacadas" class="thumbnail lazy"/><h5>
                                <a href="/story/intel-fusiona-graficos-amd-ram-cpu-unico-modulo"
                                   class="tooltip l:2856305">Intel fusiona gráficos AMD, RAM y una CPU en un único
                                    módulo</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>680</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856349.jpeg?1510009087"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="destacadas" class="thumbnail lazy"/><h5>
                                <a href="/story/rtve-rie-tu-cara-invitar-sostres-hablar-acoso"
                                   class="tooltip l:2856349">RTVE se ríe en tu cara al invitar a Sostres a hablar de
                                    acoso</a></h5></div>
                        </div>
                    </div>
                </div>
                <div class="sidebox">
                    <div>
                        <div class="header"><h4><a href="/top_visited">más visitadas</a></h4></div>
                        <div class="body">
                            <div class="cell">
                                <div class="clics"><span>17892<br/>clics</span></div>
                                <img src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855483.jpeg?1509874326"
                                     width="78" height="78" alt="más visitadas" class="thumbnail"/>  <h5><a
                                    href="/story/erotismo-oculto-campina-sovietica" class="tooltip l:2855483">El
                                erotismo oculto de la campiña soviética</a></h5></div>
                            <div class="cell">
                                <div class="clics"><span>11954<br/>clics</span></div>
                                <img src="//mnmstatic.net/cache/2b/94/media_thumb-link-2855953.jpeg?1509960786"
                                     width="78" height="78" alt="más visitadas" class="thumbnail"/>  <h5><a
                                    href="/story/humor-sinergia-sin-control-518-nunca-haria-no-abandones"
                                    class="tooltip l:2855953">Él nunca lo haría, no lo abandones</a></h5></div>
                            <div class="cell">
                                <div class="clics"><span>9301<br/>clics</span></div>
                                <img src="//mnmstatic.net/cache/2b/93/media_thumb-link-2855774.jpeg?1509913866"
                                     width="78" height="78" alt="más visitadas" class="thumbnail"/>  <h5><a
                                    href="/story/10-fenomenos-naturales-mas-extranos-existen-merecen-ser-visto"
                                    class="tooltip l:2855774">10 de los fenómenos naturales más extraños que existen y
                                que merecen ser visto al menos una vez en la vida</a></h5></div>
                            <div class="cell">
                                <div class="clics"><span>13574<br/>clics</span></div>
                                <img src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855495.jpeg?1509876966"
                                     width="78" height="78" alt="más visitadas" class="thumbnail"/>  <h5><a
                                    href="/story/asombrosa-mina-stebnyk-majestuoso-escenario-ciencia-ficcion-todo"
                                    class="tooltip l:2855495">La asombrosa mina de Stebnyk, un majestuoso escenario de
                                ciencia ficción donde todo parece estar patas arriba [ENG]</a></h5></div>
                            <div class="cell">
                                <div class="clics"><span>9300<br/>clics</span></div>
                                <img src="//mnmstatic.net/cache/2b/92/media_thumb-link-2855673.jpeg?1509901267"
                                     width="78" height="78" alt="más visitadas" class="thumbnail"/>  <h5><a
                                    href="/story/doparon-forzosamente-desde-7-anos-ahora-tiene-cuerpo-roto-mente"
                                    class="tooltip l:2855673">La doparon forzosamente desde los 7 años y ahora tiene el
                                cuerpo roto y una mente psicótica</a></h5></div>
                        </div>
                    </div>
                </div>
                <div class="sidebox red">
                    <div>
                        <div class="header"><h4><a href="/popular">más votadas</a></h4></div>
                        <div class="body">
                            <div class="cell">
                                <div class="votes"><span>787</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856352.jpeg?1510019702"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="más votadas" class="thumbnail lazy"/>
                                <h5><a href="/story/os-voy-contar-secreto-shhhh" class="tooltip l:2856352">Os voy a
                                    contar un secreto... shhhh...</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>1155</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/94/media_thumb-link-2856131.jpeg?1509980046"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="más votadas" class="thumbnail lazy"/>
                                <h5><a href="/story/portavoz-sindical-policia-madrid-entre-neonazis-insultaron"
                                       class="tooltip l:2856131">Un portavoz sindical de la Policía de Madrid, entre los
                                    neonazis que insultaron en Atocha a miembros del Parlament</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>911</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/94/media_thumb-link-2856142.jpeg?1509981666"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="más votadas" class="thumbnail lazy"/>
                                <h5><a href="/story/cospedal-rectifica-sin-disculparse-mentir-sobre-ayudas-militares"
                                       class="tooltip l:2856142">Cospedal rectifica sin disculparse por mentir sobre sus
                                    ayudas a militares franquistas</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>678</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/95/media_thumb-link-2856349.jpeg?1510009087"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="más votadas" class="thumbnail lazy"/>
                                <h5><a href="/story/rtve-rie-tu-cara-invitar-sostres-hablar-acoso"
                                       class="tooltip l:2856349">RTVE se ríe en tu cara al invitar a Sostres a hablar de
                                    acoso</a></h5></div>
                            <div class="cell">
                                <div class="votes"><span>762</span></div>
                                <img data-src="//mnmstatic.net/cache/2b/94/media_thumb-link-2855973.jpeg?1509963786"
                                     src="//mnmstatic.net/v_142/img/g.gif" alt="más votadas" class="thumbnail lazy"/>
                                <h5><a href="/story/defensa-desentiende-fosa-franquista-mas-cien-militares-leales"
                                       class="tooltip l:2855973">Defensa se desentiende de una fosa franquista con más
                                    de cien militares asesinados por permanecer leales a la República</a></h5></div>
                        </div>
                    </div>
                </div>
                <div class="sidebox">
                    <div>
                        <div class="header"><h4><span>sitios más visitados</span></h4></div>
                        <div class="body mainsites">
                            <ul>
                                <li>1. <a
                                        href="/search?q=http%3A%2F%2Fwww.eldiario.es&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.eldiario.es</a>&nbsp;<span
                                        style="font-size:80%">[15161]</span></li>
                                <li>2. <a
                                        href="/search?q=https%3A%2F%2Fwww.elconfidencial.com&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.elconfidencial.com</a>&nbsp;<span
                                        style="font-size:80%">[16320]</span></li>
                                <li>3. <a
                                        href="/search?q=https%3A%2F%2Fwww.labrujulaverde.com&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.labrujulaverde.com</a>&nbsp;<span
                                        style="font-size:80%">[13314]</span></li>
                                <li>4. <a
                                        href="/search?q=http%3A%2F%2Fwww.culturainquieta.com&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.culturainquieta.com</a>&nbsp;<span
                                        style="font-size:80%">[17890]</span></li>
                                <li>5. <a
                                        href="/search?q=http%3A%2F%2Fsinergiasincontrol.blogspot.ie&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">sinergiasincontrol.blogspot.ie</a>&nbsp;<span
                                        style="font-size:80%">[11954]</span></li>
                                <li>6. <a href="/search?q=http%3A%2F%2Fwww.bbc.com&amp;p=site&amp;h=48&amp;s=published"
                                          title="votos 48 horas:  (coef: 0)">www.bbc.com</a>&nbsp;<span
                                        style="font-size:80%">[12704]</span></li>
                                <li>7. <a
                                        href="/search?q=http%3A%2F%2Fwww.publico.es&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.publico.es</a>&nbsp;<span
                                        style="font-size:80%">[11090]</span></li>
                                <li>8. <a
                                        href="/search?q=https%3A%2F%2Fcasasincreibles.com&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">casasincreibles.com</a>&nbsp;<span
                                        style="font-size:80%">[9273]</span></li>
                                <li>9. <a
                                        href="/search?q=http%3A%2F%2Fwww.cadenaser.com&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.cadenaser.com</a>&nbsp;<span
                                        style="font-size:80%">[12817]</span></li>
                                <li>10. <a
                                        href="/search?q=http%3A%2F%2Fwww.dailymail.co.uk%2Fnews&amp;p=site&amp;h=48&amp;s=published"
                                        title="votos 48 horas:  (coef: 0)">www.dailymail.co.uk</a>&nbsp;<span
                                        style="font-size:80%">[13574]</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="sidebox">
                    <div>
                        <div class="header"><h4><a href="/cloud">etiquetas</a></h4></div>
                        <div class="body">
                            <div class="cell"><p class="tagcloud"><a style="font-size: 8pt;opacity:0.5"
                                                                     href="/search?p=tags&amp;q=bram+stoker">bram
                                stoker</a> <a style="font-size: 16.4pt;opacity:0.8"
                                              href="/search?p=tags&amp;q=catalu%C3%B1a">cataluña</a> <a
                                    style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=chilikov">chilikov</a>
                                <a style="font-size: 8pt;opacity:0.5"
                                   href="/search?p=tags&amp;q=discos+duros+de+la+sede+del+pp">discos duros de la sede
                                    del pp</a> <a style="font-size: 8pt;opacity:0.5"
                                                  href="/search?p=tags&amp;q=erotismo">erotismo</a> <a
                                        style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=explosi%C3%B3n">explosión</a>
                                <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=fotos">fotos</a> <a
                                        style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=hell+gate">hell
                                    gate</a> <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=hielo">hielo</a>
                                <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=himno+controvertido">himno
                                    controvertido</a> <a style="font-size: 8pt;opacity:0.5"
                                                         href="/search?p=tags&amp;q=jordi+%C3%A9vole">jordi évole</a> <a
                                        style="font-size: 10.8pt;opacity:0.6" href="/search?p=tags&amp;q=justicia">justicia</a>
                                <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=nueva+york">nueva
                                    york</a> <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=patinaje">patinaje</a>
                                <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=rajoy">rajoy</a> <a
                                        style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=record">record</a>
                                <a style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=rusia">rusia</a> <a
                                        style="font-size: 8pt;opacity:0.5" href="/search?p=tags&amp;q=union+europea">union
                                    europea</a> <a style="font-size: 8pt;opacity:0.5"
                                                   href="/search?p=tags&amp;q=uni%C3%B3n+sovi%C3%A9tica">unión
                                    soviética</a> <a style="font-size: 8pt;opacity:0.5"
                                                     href="/search?p=tags&amp;q=viviane+reding">viviane reding</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="newswrap">
                {promoted}
                <div class="container-fluid slider-wrapper" id="widget-popular">
                    <div class="row widget-popular-links-slider" dir="rtl">
                        <div class="link popular-link-widget-right">
                            <div class="widget-title-wrapper">
                                <div class="title"></div>
                                <div class="subtitle">ARTÍCULOS</div>
                                <div class="description">Porque tu opinión cuenta cada vez más, tenemos la plataforma
                                    para darle la visibilidad que necesita</strong></div>
                                <a class="meneame-button" href="/articles">DESCÚBRELA</a></div>
                        </div>
                        <div class="link"><a class="source"> </a>
                            <div class="title" style="clear:left;"><a href="/story/reto-30-cuentos-5-llovio-toda-noche"
                                                                      class="l:2855636">El reto de los 30 cuentos. 5.-
                                Llovió toda la noche</a></div>
                            <div class="content"><p>Esta noche la lluvia no me ha dejado dormir. Empez&oacute; como si
                                tal cosa, como algo inofensivo y sin importancia, como empiezan las cat&aacute;strofes.
                                Una gota de agua cay&oacute; sobre la punta de mi nariz. Una sola, peque&ntilde;a, min&uacute;scula,
                                nimia gotita. Casi me pareci&oacute; o&iacute;r el plic mientras rebotaba sobre la punta
                                de mi nariz y se deslizaba hacia mi p&oacute;mulo. Abr&iacute; los ojos, pero no le di
                                importancia. Creo que pens&eacute; que estaba so&ntilde;ando. Pensar que la vida es un
                                sue&ntilde;o puede ser una defensa contra lo irremediable, pero es un consuelo ef&iacute;mero.
                                Por eso cay&oacute; otra gota sobre mi nariz. Y otra. Y otra.</p>
                                <p>Me levant&eacute;. Encend&iacute; la luz. Mir&eacute; hacia arriba. El techo segu&iacute;a
                                    en su lugar habitual, a unos dos metros y medio por encima de mi cabeza, blanco,
                                    aunque un poco amarillento ya por el humo de mis cigarrillos, a pesar de que no
                                    llevaba ni tres meses en este apartamento. Pero lo m&aacute;s importante era que
                                    estaba seco, o eso parec&iacute;a. No se ve&iacute;a ninguna mancha de humedad en la
                                    zona que estaba sobre mi cabeza, ni en ninguna otra parte del techo en realidad.
                                    Decid&iacute; que el techo estaba seco, aunque eso no me gustaba porque, si las
                                    gotitas, peque&ntilde;as, min&uacute;sculas, inofensivas, s&iacute;, pero h&uacute;medas
                                    y molestas al fin y al cabo que hab&iacute;an ca&iacute;do sobre mi nariz no proven&iacute;an
                                    del techo &iquest;de d&oacute;nde ven&iacute;an?</p>
                                <p>Se me ocurri&oacute; que a lo mejor hab&iacute;a llorado en sue&ntilde;os. Esa idea
                                    no me gustaba nada en absoluto. Adem&aacute;s &iquest;estaba realmente dormido
                                    cuando cay&oacute; la primera gota sobre mi cara? No, no estaba dormido. Estaba
                                    recordando la noche que conoc&iacute; a Carla, el cruce de miradas en la cola de la
                                    filmoteca, la sonrisa inevitable, la decisi&oacute;n no s&eacute; si suya, m&iacute;a
                                    o de ambos, de sentarnos juntos. Y despu&eacute;s, al salir, la noche que se hizo
                                    eterna entre vinos y cigarrillos, cerrando bares, m&aacute;s ebrios de conversaci&oacute;n
                                    que de alcohol. La lluvia prodigiosa al borde del amanecer, cuando el domingo naci&oacute;
                                    arcoiris y nos llev&oacute;, indiscutible, a dormir muy juntos en su casa, sin hacer
                                    el amor, cansados ya de tanto como &iacute;bamos a querernos.</p>
                                <p>Es cierto, llovi&oacute; al amanecer, al final de aquella noche que parec&iacute;a
                                    que no iba a acabarse nunca. Amaneci&oacute; tan despacio que nos dio tiempo de
                                    llegar a su casa antes de que fuera de d&iacute;a, bajo aquella lluvia fina como la
                                    risa de Carla, que se met&iacute;a bajo mi piel y se mezclaba con mi sangre espesa,
                                    alivi&aacute;ndome del peso de la vida.</p>
                                <p>Plantado en mitad de mi habitaci&oacute;n, en calzoncillos, recordando, me sent&iacute;
                                    un poco idiota y tuve sed. En la cocina, mientras el agua corr&iacute;a por el
                                    fregadero, con el vaso en la mano, sent&iacute; como me ca&iacute;a una gota de agua
                                    en la nuca y se deslizaba por mi espalda. Cerr&eacute; el grifo, como si hubiera
                                    alguna relaci&oacute;n entre el agua del grifo y la que, innegable, acababa de
                                    mojarme el cuello. Mir&eacute; hacia arriba. Nada. Bueno, no exactamente. Parec&iacute;a
                                    como si un cristal flotara a media altura sobre mi cabeza. No se ve&iacute;a nada en
                                    realidad, pero hab&iacute;a un trozo del aire que parec&iacute;a diferente, como si
                                    tuviera una textura m&aacute;s espesa de lo normal.</p>
                                <p>Me cay&oacute; una gota de agua en el ojo. Ven&iacute;a directamente de ese defecto
                                    del aire que estaba mirando. Ahora no ten&iacute;a ninguna duda. Sobre mi cabeza
                                    flotaba una l&aacute;mina de agua, no muy grande, del tama&ntilde;o de mi mano, m&aacute;s
                                    o menos. Me qued&eacute; mirando atentamente, calculando sus dimensiones a partir
                                    del modo en que deformaba el aire. Al principio no era f&aacute;cil distinguir los
                                    bordes, pero al cabo de un momento el ojo se acostumbraba a la sutil diferencia en
                                    la consistencia del aire. Era como si en ese punto en concreto alguien hubiera
                                    colgado un cristal graduado, pero con una graduaci&oacute;n muy baja. Mientras
                                    observaba y me preguntaba de d&oacute;nde vendr&iacute;a esa l&aacute;mina de agua
                                    que flotaba sobre mi cabeza, esta se deshizo en una peque&ntilde;a lluvia. No puedo
                                    explicarlo de otra forma. Me llovi&oacute; encima. Una lluvia fina, breve y
                                    explosiva, como una peque&ntilde;a carcajada. La cantidad de agua que me cay&oacute;
                                    encima equival&iacute;a, m&aacute;s o menos, a un vaso de agua. Me empap&oacute; la
                                    cabeza y los hombros, por supuesto. Mir&eacute; el vaso de cristal que todav&iacute;a
                                    ten&iacute;a en la mano, vac&iacute;o, como si en &eacute;l hubiera alguna explicaci&oacute;n
                                    a lo que estaba pasando, pero no la encontr&eacute;.</p>
                                <p>Encend&iacute; todas las luces de la casa, camino del ba&ntilde;o donde cog&iacute;
                                    una toalla. Iba observando cuidadosamente el techo, en busca de otro de esos charcos
                                    flotantes, de esas anomal&iacute;as transparentes que deformaban la luz a su
                                    alrededor como si fueran sonrisas colgadas del techo, pero no encontr&eacute;
                                    ninguna. Sal&iacute; del ba&ntilde;o con la toalla sobre los hombros y me dirig&iacute;
                                    al sal&oacute;n en busca de un cigarrillo. Busqu&eacute; el mechero sobre la mesa,
                                    apartando los folios manchados y las fotograf&iacute;as boca abajo sobre cuyas
                                    espaldas se le&iacute;an fechas y peque&ntilde;as frases. All&iacute; estaba el
                                    mechero. Rojo carm&iacute;n. Encend&iacute; el cigarrillo y me acerqu&eacute; a la
                                    ventana. Apenas pasaban ya coches y se dir&iacute;a que a la luz de las farolas le
                                    costaba llegar al suelo. Deb&iacute;a de ser uno de esos momentos absurdos de mitad
                                    de la madrugada, entre las tres y las cuatro, cuando parece que las cosas existen de
                                    otra manera.</p>
                                <p>De pronto me cay&oacute; un chaparr&oacute;n. No puedo definirlo de otra forma. Empez&oacute;
                                    a llover en todo el sal&oacute;n. El charco, porque en ning&uacute;n momento vi
                                    nubes, sino tan solo esa especie de charcos flotantes a media altura sobre mi
                                    cabeza, el charco, digo, debi&oacute; haberse formado mientras yo estaba despistado
                                    buscando el mechero color carm&iacute;n, cuando no quer&iacute;a mirar el rostro de
                                    las fotograf&iacute;as, mientras miraba por la ventana sin recordar nada en
                                    especial. Nada en especial. Y llov&iacute;a a base de bien. Pero la lluvia ca&iacute;a
                                    de una forma extra&ntilde;a, lenta, suave, como si fuera el propio aire el que se
                                    deshac&iacute;a sobre mi cabeza en forma de gotas. Me cubr&iacute; con la toalla y
                                    sal&iacute; corriendo del sal&oacute;n.</p>
                                <p>Volv&iacute; a la habitaci&oacute;n y me ech&eacute; sobre la cama. Hab&iacute;a
                                    llevado los cigarrillos carm&iacute;n conmigo y encend&iacute; otro, mirando al
                                    techo. Me pregunt&eacute;, de la forma m&aacute;s l&oacute;gica y racional que fui
                                    capaz, si estar&iacute;a durmiendo. Me respond&iacute; que era la &uacute;nica
                                    explicaci&oacute;n sensata a lo que estaba pasando. M&aacute;s tranquilo al saber
                                    que todo era un sue&ntilde;o, di una profunda calada al cigarrillo y expuls&eacute;
                                    el humo hacia el techo. Vi como el humo se deten&iacute;a a medio camino, como si
                                    hubiera tropezado con un cristal, y supe con medio segundo de antelaci&oacute;n que
                                    iba a llover sobre mi cama, como as&iacute; fue.</p>
                                <p>Me levant&eacute; de un salto y me apart&eacute; un poco, justo para vez c&oacute;mo
                                    la lluvia ca&iacute;a justo sobre el colch&oacute;n y ni una sola gota fuera de la
                                    cama. El suelo alrededor estaba completamente seco, mientras el colch&oacute;n iba
                                    empap&aacute;ndose dulcemente y sobre las s&aacute;banas se formaban peque&ntilde;os
                                    charcos con forma de sonrisas.</p>
                                <p>De nuevo en la cocina, busqu&eacute; la botella de ron. Estaba casi vac&iacute;a,
                                    pero hubo suficiente para llenar hasta la mitad el vaso en el que no llegu&eacute; a
                                    beber agua un rato antes. Lo vaci&eacute; de dos grandes sorbos. Me pregunt&eacute;
                                    qu&eacute; se puede hacer en una situaci&oacute;n como esa. Un peque&ntilde;o
                                    chubasco completamente absurdo me dio la respuesta.</p>
                                <p>Fui a la habitaci&oacute;n. Por el pasillo llov&iacute;a como cuando los ni&ntilde;os
                                    se re&iacute;an de m&iacute; en el colegio, pero en el sal&oacute;n ca&iacute;a un
                                    chaparr&oacute;n que se parec&iacute;a al descubierto que no hab&iacute;a parado de
                                    crecer en mi cuenta bancaria en las &uacute;ltimas semanas. Al pasar por el ba&ntilde;o
                                    vi que all&iacute; llov&iacute;a como si fuera primavera, tal vez porque ol&iacute;a
                                    al jab&oacute;n de ba&ntilde;o floral de Carla. En la habitaci&oacute;n me pus&eacute;
                                    el chubasquero del color de los ojos azules como los ojos de Carla. Llov&iacute;a a
                                    carcajadas sobre la cama cuando me ech&eacute; sobre el colch&oacute;n empapado y no
                                    par&oacute; de llover durante toda la noche, por toda la casa, mientras yo lloraba
                                    por &uacute;ltima vez a Carla.</p>
                                <p></p></div>
                            <div class="link-info"><span data-ts="1509896123" class="ts visible time" title="enviado: ">____</span>
                                <span style="font-size: 10px;">&mdash;</span> <a href="/user/personare"
                                                                                 class="author tooltip u:354522">personare</a>
                            </div>
                        </div>
                        <div class="link"><a class="source"> </a>
                            <div class="title" style="clear:left;"><a href="/story/sobre-cortinas-humo"
                                                                      class="l:2855551">Sobre las cortinas de humo</a>
                            </div>
                            <div class="content"><p>Una cortina de humo es un conjunto de hechos o circunstancias,
                                ficticios o reales, con los que se pretende ocultar las verdaderas intenciones o desviar
                                la atenci&oacute;n de los dem&aacute;s. Todo aquello que sirva para evitar que la gente
                                sepa o vea lo importante, constituye una cortina de humo.</p>
                                <p>Nadie va a negar que esto existe (solo va a negar que algo en concreto es una cortina
                                    de humo, pero de otra cosa si dir&aacute; que es una cortina de humo) y que
                                    realmente es efectivo, que tiene sentido hacerlo, que no se hace por hobby.</p>
                                <p>Pero cada vez que leo un comentario en alguna noticia de Catalu&ntilde;a diciendo que
                                    es una cortina de humo para que no se hable de la corrupci&oacute;n del PP/Ciu, o de
                                    lo de Murcia, o de las huelgas como la de Bershka y de las trabajadoras de las
                                    residencias de Bizkaia, no puedo evitar pensar &ldquo;&iquest;y si se hablara de eso
                                    qu&eacute;?&rdquo;</p>
                                <p>Y es que de la corrupci&oacute;n se ha hablado largo y tendido (incluso en la tele),
                                    es con frecuencia la principal preocupaci&oacute;n de los espa&ntilde;oles seg&uacute;n
                                    el bar&oacute;metro del CIS, turn&aacute;ndose con el paro (otra cosa de la que se
                                    supone nos evita hablar las cortinas de humo). &iquest;Y? &iquest;a cuantas
                                    conversaciones sobre corrupci&oacute;n nos hemos quedado de eliminarla? Porque
                                    parece que esta es la idea, eliminar la corrupci&oacute;n hablando de ella.</p>
                                <p>Las trabajadoras de las residencias de Bizkaia, las de Bershka y la gente de Murcia
                                    han conseguido buena parte de sus objetivos. Es seguro que estas personas estaban
                                    igual de informadas sobre lo que pasaba en Catalu&ntilde;a que el resto de la naci&oacute;n,
                                    solo que probablemente se enteraban de cada cosa solo una vez, no mil millones de
                                    veces, porque cuando uno esta ocupado tirando un muro abajo no tiene mucho tiempo
                                    para entretenerse.</p>
                                <p>Esta gente no salio a la calle porque en sus televisores echen otra cosa
                                    sustancialmente distinta a lo que vemos el resto cuando la encendemos. Estas
                                    reivindicaciones no salieron adelante porque las televisaran, todo el mundo se
                                    enterara y todos habl&aacute;ramos de ellas, salieron adelante porque hab&iacute;a
                                    gente luchando por ellas (condici&oacute;n no siempre suficiente, pero si la
                                    &uacute;nica que es realmente necesaria).</p>
                                <p>&iquest;Qu&eacute; clase de consuelo es para una empresa no salir en la tele cuando
                                    tiene parte de su actividad econ&oacute;mica paralizada por una huelga? Pues si,
                                    mejor que no salga en la tele, pero eso no va a evitar que todo se vaya al carajo si
                                    los trabajadores no vuelven, y lo que va a posibilitar que no vuelvan es la caja de
                                    resistencia, no los minutos que salgan en el noticiario.</p>
                                <p>&iquest;Qu&eacute; clase de alivio es para un gobierno que no se hable de corrupci&oacute;n?
                                    Pues un extra, pero lo que va a mantener su chiringuito es la pasividad de la gente,
                                    no que no se hable de ello, hay demasiadas pruebas emp&iacute;ricas de que hablar de
                                    corrupci&oacute;n es perfectamente compatible con la corrupci&oacute;n. Incluso a
                                    veces parece que las noticias sobre corrupci&oacute;n son la cortina de humo de la
                                    propia corrupci&oacute;n.</p>
                                <p>Creo que el inter&eacute;s que tenemos sobre que se hable de un tema es una esperanza
                                    que exista un efecto contagio o un efecto alentador. Por ejemplo:</p>
                                <ul>
                                    <li>Si se habla de lo de Bershka cundir&aacute; el ejemplo y otros har&aacute;n lo
                                        mismo.
                                    </li>
                                    <li>Si se habla de lo de Murcia las protestas no cesar&aacute;n porque se sentir&aacute;n
                                        apoyados.
                                    </li>
                                </ul>
                                <p>&iquest;Pero esto tiene sentido? Vuelvo a repetir, &iquest;es que la gente movilizada
                                    cuando pone la tele ve algo distinto a lo que vemos los dem&aacute;s? La gente de
                                    Bershka no ha hecho huelga porque lo haya visto antes en la tele. La gente de Murcia
                                    no ha conseguido el soterramiento del tren porque haya habido tertulias a gritos
                                    sobre ello con Inda y la dem&aacute;s panda o porque haya intervenido la ONU.</p>
                                <p>&iquest;Cual es la idea? &iquest;Por cada X conversaciones sobre un tema me ahorro
                                    una acci&oacute;n directa?</p>
                                <p>&ldquo;- Tome, 24 horas de prime time sobre lo de Bershka - Genial, con eso nos
                                    ahorramos un d&iacute;a de huelga&rdquo;</p>
                                <p>Si lo vemos as&iacute; esta claro que con todo lo que se ha hablado de corrupci&oacute;n
                                    esta deber&iacute;a haber desaparecido sin necesidad de mover un dedo. No es el
                                    caso, de hecho lo poco que se ha avanzado contra la corrupci&oacute;n ha sido a base
                                    de acciones directas, no de hablar y hablar y hablar.</p>
                                <p>Y cuidado, no niego el impacto de los medios (o llegados a este punto, de las
                                    conversaciones) lo que niego es que convaliden cr&eacute;ditos de movilizaci&oacute;n,
                                    niego que sean una condici&oacute;n necesaria, niego que una persona que no hace
                                    nada sea mejor si habla de X que de Z, &iquest;qu&eacute; m&aacute;s de que hable si
                                    no va a hacer nada?.</p>
                                <p>Imaginen un escenario donde el monotema de los &uacute;ltimos meses hubiera sido lo
                                    de Murcia, y que esto hubiera eclipsado lo de Catalu&ntilde;a. No veo en absoluto
                                    descabellado que en tal caso se dijera que lo de Murcia era una cortina de humo para
                                    tapar lo de Catalu&ntilde;a, y tendr&iacute;amos a la gente que no hace nada en vez
                                    de hablando de Catalu&ntilde;a hablando de Murcia, sin embargo la gente que si esta
                                    movilizada seguir&iacute;a haciendo lo mismo que esta haciendo ahora.</p>
                                <p>Quiz&aacute; lo que esperamos de que todo el mundo hable de lo de Bershka es que deje
                                    de comprar ah&iacute;, o que todo el mundo hable de corrupci&oacute;n es que deje de
                                    votar partidos corruptos, pero eso no es solo hablar, eso es mucho m&aacute;s, y si,
                                    puede que ayude que un tema este en el candelero pero seamos sinceros, la gente no
                                    se vuelve activista porque lo haya visto en la tele. Lo que pueda salir de ah&iacute;
                                    es un &ldquo;bonus inesperado&rdquo;, si pasa guay, no lo vamos a rechazar, todo
                                    ayuda, pero no se puede fundamentar un cambio de esa envergadura en semejante cosa,
                                    no se puede hacer de ello una condici&oacute;n necesaria. Es infantil y no va a
                                    suceder, las cortinas de humo no desaparecer&aacute;n primero y luego, como
                                    consecuencia, la gente se movilizara, si no al rev&eacute;s, la gente se movilizara
                                    y luego, como consecuencia, las cortinas de humo ser&aacute;n irrelevantes, como se
                                    ha visto en el caso de Murcia, Bershka y las trabajadoras de las residencias de
                                    Bizkaia.</p>
                                <p>O quiz&aacute; lo que esperamos de que todo el mundo hable de las luchas de los dem&aacute;s,
                                    que est&eacute;n todo el rato en la tele, es que las &eacute;lites tengan miedo, se
                                    lleven la idea infundada (a d&iacute;a de hoy) de que el grueso de la poblaci&oacute;n
                                    es as&iacute;, que el problema que se han encontrado en Bershka, Murcia y Bizkaia se
                                    puede generalizar y que mejor aflojar antes de que esto suceda, quiz&aacute; lo que
                                    esperamos es beneficiarnos de las luchas de otros sin tener que llegar a luchar
                                    nosotros mismos, quiz&aacute; no tanto pero alguna migaja que caiga... alguna
                                    facilidad extra&hellip; algo, lo que sea. Que el inter&eacute;s en que no haya
                                    cortinas de humo no es en movilizarse, si no en todo lo contrario, en evitar tener
                                    que hacerlo porque deje de ser necesario, porque con menos movilizaci&oacute;n se
                                    saque m&aacute;s, porque con la movilizaci&oacute;n de unos pocos vivamos el resto.
                                    Y no es descabellado entender porque alguien va a pensar as&iacute;, al fin y al
                                    cabo la jornada de 8 horas no fue solo para los que lucharon por ella, tambi&eacute;n
                                    la obtuvieron los dem&aacute;s. Pero eso es&hellip; en fin, todos sabemos como
                                    calificar esa manera de pensar y actuar.</p></div>
                            <div class="link-info"><span data-ts="1509883348" class="ts visible time" title="enviado: ">____</span>
                                <span style="font-size: 10px;">&mdash;</span> <a href="/user/kdekilo"
                                                                                 class="author tooltip u:563777">kdekilo</a>
                            </div>
                        </div>
                        <div class="link"><a class="source"> </a>
                            <div class="title" style="clear:left;"><a href="/story/filtrar-meneos" class="l:2855803">Filtrar
                                meneos</a></div>
                            <div class="content"><p>Lo mismo ya es mucho copiarse del reddit, pero se podr&iacute;a
                                poner un filtro de "temas dominantes", como en worldnews. Por ejemplo, filtrar para que
                                no se vean meneos de "el tema".</p></div>
                            <div class="link-info"><span data-ts="1509916695" class="ts visible time" title="enviado: ">____</span>
                                <span style="font-size: 10px;">&mdash;</span> <a href="/user/el_vago"
                                                                                 class="author tooltip u:544499">el_vago</a>
                            </div>
                        </div>
                        <div class="link"><a class="source"> </a>
                            <div class="title" style="clear:left;"><a
                                    href="/story/gallego-multiples-formas-decir-esta-lloviendo" class="l:2840806">El
                                gallego y sus múltiples formas de decir que está lloviendo</a></div>
                            <div class="content"><p><img
                                    src="https://www.meneame.net/backend/media?type=link&amp;id=2840806&amp;version=0&amp;ts=0&amp;image.jpeg">
                            </p>
                                <p>Dicen que la lluvia en Galicia es arte, o eso es lo que proclama Siniestro Total en
                                    la canci&oacute;n Mi&ntilde;a terra galega. Tambi&eacute;n dicen que siempre llueve
                                    pero os aseguro que no es para tanto, ahora mismo desde la ventana veo el sol. Y no,
                                    no somos Galifornia. Pongamos fin a ese terrible t&eacute;rmino, por favor.</p>
                                <p>M&aacute;s all&aacute; de si la lluvia arte o no, queda claro que las precipitaciones
                                    son una parte importante de la vida de los gallegos: tenemos un mont&oacute;n de
                                    palabras para designar la lluvia seg&uacute;n su intensidad, hay quien <a
                                            href="http://www.gciencia.com/tolociencia/61-palabras-en-galego-para-designar-a-choiva/">dicen
                                        que 61</a>, otros se&ntilde;alan que incluso son m&aacute;s de 100. La fil&oacute;loga
                                    <a href="http://revistas.um.es/estudiosromanicos/article/view/78481/75791">Elvira
                                        Fidalgo</a> ha investigado hecho su tesis sobre la formaci&oacute;n de las
                                    palabras en gallego para designar la lluvia. Os hago un adelanto: <strong>&uacute;nicamente
                                        se necesitaron cinco palabras de origen lat&iacute;n y griego para formarse la
                                        mayor&iacute;a los t&eacute;rminos y expresiones que hoy en d&iacute;a
                                        conocemos.</strong></p>
                                <p>Os puedo asegurar que a d&iacute;a de hoy no las he usado todas, pero no est&aacute;
                                    de m&aacute;s conocerlas y compartirlas por si a alguien le interesar. Si os pica la
                                    curiosidad sobre lo que significa exactamente cada una de las palabras que vais a
                                    leer a continuaci&oacute;n, os recomiendo hacer uso del diccionario online de la <a
                                            href="http://academia.gal/dicionario/">Real Academia Galega</a>.</p>
                                <p><strong>Sin duda alguna, la lluvia fina es el tipo de lluvia que m&aacute;s palabras
                                    cuenta para designarla</strong>: Puede ser orballo, orballeira, orballada, chuvisco,
                                    chuviscada, chuvi&ntilde;a, chuvi&ntilde;ada pero tambi&eacute;n palabras derivadas
                                    del lexema bab- como babu&ntilde;a, babuxa, barballa, barba&ntilde;a, barba&ntilde;eiro,
                                    barbu&ntilde;a, barbuza, barrallo... Y de &ldquo;pulvis&rdquo; poalla, poalleira y
                                    poallada. Adem&aacute;s de otras como zarzallo, pati&ntilde;eira, mexadeira,
                                    mollaparvos, mexaparvos...</p>
                                <p>Tambi&eacute;n diferenciamos cuando la lluvia viene acompa&ntilde;ada de hielo o
                                    granizo con palabras como auganeve, calistro, cebrina, corisco, cebrisca,
                                    escarabana, nevada, nevarada, nevareira, nevar&iacute;o, nevisca, nevarisca,
                                    pedrazo, salabreada, sarabiada o torba.</p>
                                <p>Para designar las situaciones en las que llueve mucho, usamos palabras que derivan de
                                    &ldquo;bullar&rdquo; como ball&oacute;n, balloada, b&aacute;tega o bategada. Usamos
                                    chuvasco, chaparrada o cebrina para lluvias intensas y de corta duraci&oacute;n. En
                                    mi pueblo, Cangas do Morrazo, lo llamamos tambi&eacute;n cairo, una palabra que jam&aacute;s
                                    he o&iacute;do m&aacute;s all&aacute; de las fronteras de la pen&iacute;nsula del
                                    Morrazo. Si hay alg&uacute;n gallego por aqu&iacute;, que se pronuncie. </p>
                                <p>&iquest;Y qu&eacute; pasa cuando hay lluvia acompa&ntilde;ada de rayos y truenos?
                                    Usamos las palabras derivadas de &ldquo;turbo&rdquo; como treb&oacute;n, torb&oacute;n,
                                    treboada, torboada. Si piensas que esto se hab&iacute;a acabado, a&uacute;n tenemos
                                    m&aacute;s.Aqu&iacute; va la traca final: si la lluvia viene acompa&ntilde;ada de
                                    vientos fuertes: brea, cifra, cebra, cebrina, ciobra, zarracina. Incluso para esa
                                    niebla que moja como mera, salseiro, borraxeira, cego&ntilde;a o fuscallo. </p>
                                <p>Si conoc&eacute;is alguna palabra m&aacute;s para designar la lluvia en gallego, pod&eacute;is
                                    dejarla en los comentarios y estar&eacute; encantada de a&ntilde;adirla :) </p>
                                <p></p></div>
                            <div class="link-info"><span data-ts="1509989313" class="ts visible time" title="enviado: ">____</span>
                                <span style="font-size: 10px;">&mdash;</span> <a href="/user/yuhu"
                                                                                 class="author tooltip u:518162">yuhu</a>
                            </div>
                        </div>
                        <div class="link"><a class="source"> </a>
                            <div class="title" style="clear:left;"><a href="/story/reto-30-cuentos-4-bucle"
                                                                      class="l:2855186">El reto de los 30 cuentos. 4.-
                                Bucle</a></div>
                            <div class="content"><p>Todos estos a&ntilde;os de investigaci&oacute;n hab&iacute;an dado
                                su fruto. En sus manos ten&iacute;a el poder de controlar el tiempo a peque&ntilde;a
                                escala. Pulsando el &uacute;nico bot&oacute;n de esa peque&ntilde;a caja retroceder&iacute;a
                                10 segundos en el tiempo. Ya no iba a tener m&aacute;s problemas para relacionarse con
                                la gente. Si met&iacute;a la pata como estaba acostumbrado a hacer, pulsando ese bot&oacute;n
                                se podr&iacute;a arreglar.</p>
                                <p>Ahora solo faltaba asegurarse de que su invento funcionaba a la perfecci&oacute;n.
                                    Puls&oacute; el bot&oacute;n.</p>
                                <p></p>
                                <p>Todos estos a&ntilde;os de investigaci&oacute;n hab&iacute;an dado su fruto. En sus
                                    manos ten&iacute;a el poder de controlar el tiempo a peque&ntilde;a escala. Pulsando
                                    el &uacute;nico bot&oacute;n de esa peque&ntilde;a caja retroceder&iacute;a 10
                                    segundos en el tiempo. Ya no iba a tener m&aacute;s problemas para relacionarse con
                                    la gente. Si met&iacute;a la pata como estaba acostumbrado a hacer, pulsando ese bot&oacute;n
                                    se podr&iacute;a arreglar.</p>
                                <p>Ahora solo faltaba asegurarse de que su invento funcionaba a la perfecci&oacute;n.
                                    Puls&oacute; el bot&oacute;n.</p>
                                <p></p>
                                <p>Todos estos a&ntilde;os de investigaci&oacute;n hab&iacute;an dado su fruto. En sus
                                    manos ten&iacute;a el poder de controlar el tiempo a peque&ntilde;a escala. Pulsando
                                    el &uacute;nico bot&oacute;n de esa peque&ntilde;a caja retroceder&iacute;a 10
                                    segundos en el tiempo. Ya no iba a tener m&aacute;s problemas para relacionarse con
                                    la gente. Si met&iacute;a la pata como estaba acostumbrado a hacer, pulsando ese bot&oacute;n
                                    se podr&iacute;a arreglar.</p>
                                <p>Ahora solo faltaba asegurarse de que su invento funcionaba a la perfecci&oacute;n.
                                    Puls&oacute; el bot&oacute;n.</p>
                                <p></p></div>
                            <div class="link-info"><span data-ts="1509804047" class="ts visible time" title="enviado: ">____</span>
                                <span style="font-size: 10px;">&mdash;</span> <a href="/user/personare"
                                                                                 class="author tooltip u:354522">personare</a>
                            </div>
                        </div>
                    </div>
                    <div class="dots"></div>
                    <div style="display:none;">
                        <div class="slick-prev"></div>
                        <div class="slick-next"></div>
                    </div>
                </div>
                {meneos}

                <div class="pages margin"><a href="?page=7059" rel="nofollow" rel="prev">&#171; anterior</a><a
                        href="?page=1" title="ir a página 1">1</a><span>&hellip;</span><a href="?page=7058"
                                                                                          title="ir a página 7058"
                                                                                          rel="nofollow">7058</a><a
                        href="?page=7059" title="ir a página 7059" rel="nofollow">7059</a><span
                        class="current">7060</span><span class="nextprev">&#187; siguiente</span></div>
            </div>
            <div id="footwrap">
                <div id="footcol1"><h5>suscripciones por RSS</h5>
                    <ul>
                        <li><a href="/rss">publicadas</a></li>
                        <li><a href="/rss?status=queued">en cola</a></li>
                        <li><a href="/rss?active">más activas</a></li>
                        <li><a href="/comments_rss">todos los comentarios</a></li>
                    </ul>
                </div>
                <div id="footcol2"><h5>ayuda</h5>
                    <ul id="helplist">
                        <li><a href="/faq-es">faq</a></li>
                        <li><a href="http://meneame.wikispaces.com/Ayuda">ayuda</a></li>
                        <li><a href="http://meneame.wikispaces.com/">wiki</a></li>
                        <li><a href="http://meneame.wikispaces.com/Bugs">avisar errores</a></li>
                        <li><a href="/legal#contact">avisar abusos</a></li>
                    </ul>
                </div>
                <div id="footcol3"><h5>+menéame</h5>
                    <ul id="moremenelist">
                        <li><a href="/novedades-en-meneame">novedades</a></li>
                        <li><a href="/trends">tendencias</a></li>
                        <li><a href="http://twitter.com/meneame_net">síguenos en twitter</a></li>
                        <li><a href="/notame/">nótame</a></li>
                        <li><a href="http://blog.meneame.net/">blog</a></li>
                    </ul>
                </div>
                <div id="footcol4"><h5>estadísticas</h5>
                    <ul id="statisticslist">
                        <li><a href="/popular">populares</a></li>
                        <li><a href="/top_commented">más comentadas</a></li>
                        <li><a href="/top_comments">mejores comentarios</a></li>
                        <li><a href="/cloud">nube de etiquetas</a></li>
                        <li><a href="/sites_cloud">nube de webs</a></li>
                        <li><a href="/promote">candidatas</a></li>
                        <li><a href="/values">parámetros básicos</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div id="footthingy"><p>menéame</p>
            <ul id="legalese">
                <li><a href="/legal">condiciones legales</a> &nbsp;&#47;&nbsp;<a href="/legal#tos">de uso</a> &nbsp;&#47;&nbsp;<a
                        href="/legal#cookies">y de cookies</a></li>
                <li>&nbsp;&#47;&nbsp;<a href="/faq-es#we">quiénes somos</a></li>
                <li>&nbsp;&#47;&nbsp;licencias:&nbsp; <a href="/COPYING">código</a>,&nbsp; <a
                        href="https://creativecommons.org/licenses/by-sa/3.0/">gráficos</a>,&nbsp; <a rel="license"
                                                                                                      href="https://creativecommons.org/licenses/by/3.0/es/">contenido</a>
                </li>
                <li>&nbsp;&#47;&nbsp;<a href="https://validator.w3.org/nu/?doc=https:/www.meneame.net">HTML5</a></li>
                <li>&nbsp;&#47;&nbsp;<a href="https://github.com/gallir/Meneame">codigo fuente</a></li>
            </ul>
        </div>
    </div>
</div>
<div id='backTop'></div>
<!--[if lt IE 9]>
</html>
"""

MENEO = """
<div class="news-summary">
    <div class="news-body">
        <div class="news-shakeit mnm-published">
            <div class="votes"><a href="/story/ruby-off-the-rails" id="a-votes-1382">{votes}</a> meneos</div>
            <div class="menealo" id="a-va-1382"><span class="closed">cerrado</span></div>
            <div class="clics">  </div>
        </div>
        <div class="center-content no-padding"><h2><a class="l:1382"
                                                      href="http://www-128.ibm.com/developerworks/library/j-ruby/?ca=dgr-lnxw01RubyOffRails">
            {title} </a></h2>
            <div class="news-submitted"><a class="tooltip u:41" href="/user/{author}"><img alt="{author}" class="lazy"
                                                                                       data-2x="s:-25.:-40."
                                                                                       data-src="/cache/00/00/41-1241311647-25.jpg"
                                                                                       src="https://mnmstatic.net/v_142/img/g.gif"/></a>
                por <a href="/user/{author}/history">{author}</a> a <span class="showmytitle"
                                                                  title="http://www-128.ibm.com/developerworks/library/j-ruby/?ca=dgr-lnxw01RubyOffRails">www-128.ibm.com</span>
                  <span class="ts visible" data-ts="1135515250" title="enviado: ">____</span> publicado: <span
                        class="ts visible" data-ts="1135542302" title="publicado: ">____</span></div>
            <div class="news-content">Interesante artículo de IBM Developer Works sobre ruby (sin Rails) claramente
                orientado a programadores de Java
            </div>
        </div>
        <div class="news-details">
            <div class="news-details-data-up"><span class="votes-up" data-placement="top" data-toggle="tooltip"
                                                    title="Votos positivos"><i class="fa fa-arrow-circle-up"></i> <span
                    id="a-usu-1382"><strong>{votes}</strong></span></span> <span class="wideonly votes-anonymous"
                                                                            data-placement="top" data-toggle="tooltip"
                                                                            title="Votos anónimos"><i
                    class="fa fa-user-secret"></i> <span id="a-ano-1382"><strong>0</strong></span></span> <span
                    class="votes-down" data-placement="top" data-toggle="tooltip" title="Votos negativos"><i
                    class="fa fa-arrow-circle-down"></i> <span id="a-neg-1382"><strong>0</strong></span></span> <span
                    class="tool karma" data-placement="top" data-toggle="tooltip" title="Karma"> <span
                    class="karma-letter">K</span> <span class="karma-value" id="a-karma-1382">  165  </span> </span>
                <span class="tool sub-name"> <a class="subname" href="/m/mnm">mnm</a> </span></div>
            <div class="news-details-main"><a class="comments" href="/story/ruby-off-the-rails"
                                              title="comentarios de: «{title}»"> <i
                    class="fa fa-comments"></i>sin comentarios </a>
                <button class="social-share"><i class="fa fa-share-alt"></i>compartir</button>
                <div class="wrapper-share-icons hide">
                    <ul class="share-icons" data-title="{title}"
                        data-url="https://www.meneame.net/story/ruby-off-the-rails">
                        <li><a class="share-facebook" href="#" onclick="share_fb(this)"><i
                                class="fa fa-facebook-square"></i>Compartir en Facebook</a></li>
                        <li><a class="share-twitter" href="#" onclick="share_tw(this)"><i
                                class="fa fa-twitter-square"></i>Compartir en Twitter</a></li>
                        <li><a class="share-mail"
                               href="mailto:?subject={title}&amp;body=https%3A%2F%2Fwww.meneame.net%2Fstory%2Fruby-off-the-rails"
                               title="Compartir por Correo"><i class="fa fa-envelope"></i>Compartir por Correo</a></li>
                        <li>
                            <button class="share-link" data-clipboard-text="http://menea.me/12e"><i
                                    class="fa fa-link"></i><span>Copiar enlace</span></button>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="news-details-data-down"><span class="votes-up" data-placement="top" data-toggle="tooltip"
                                                      title="Votos positivos"><i
                    class="fa fa-arrow-circle-up"></i> <span id="a-usu-1382"><strong>{votes}</strong></span></span> <span
                    class="wideonly votes-anonymous" data-placement="top" data-toggle="tooltip"
                    title="Votos anónimos"><i class="fa fa-user-secret"></i> <span
                    id="a-ano-1382"><strong>0</strong></span></span> <span class="votes-down" data-placement="top"
                                                                           data-toggle="tooltip"
                                                                           title="Votos negativos"><i
                    class="fa fa-arrow-circle-down"></i> <span id="a-neg-1382"><strong>0</strong></span></span> <span
                    class="tool karma" data-placement="top" data-toggle="tooltip" title="Karma"> <span
                    class="karma-letter">K</span> <span class="karma-value" id="a-karma-1382">  165  </span> </span>
                <span class="tool sub-name"> <a class="subname" href="/m/mnm">mnm</a> </span></div>
        </div>
    </div>
</div>
"""
PROMOTED = """
<div class="news-summary promoted-article">
    <div class="news-body">
        <div class="news-shakeit mnm-queued">
            <div class="votes"><a id="a-votes-2855636"
                                  href="/story/reto-30-cuentos-5-llovio-toda-noche">87</a> meneos
            </div>
            <div class="menealo" id="a-va-2855636"><a href="javascript:menealo(0, 2855636)"
                                                      id="a-shake-2855636">menéalo</a></div>
            <div class="clics"> 1247 clics</div>
        </div>
        <div class="warn tooltip w:2855636"> Este envío tiene varios votos negativos. <a
                href="/story/reto-30-cuentos-5-llovio-toda-noche">Asegúrate</a> antes de menear
        </div>
        <div class="tab-promoted-article">ARTÍCULO</div>
        <div class="center-content no-padding"><h2><a
                href="https://www.meneame.net/story/reto-30-cuentos-5-llovio-toda-noche"
                class="l:2855636">El reto de los 30 cuentos. 5.- Llovió toda la noche</a></h2>
            <div class="news-submitted"><a href="/user/personare" class="tooltip u:354522"><img
                    src="https://mnmstatic.net/v_142/img/g.gif"
                    data-src="/cache/05/68/354522-1355384589-25.jpg" data-2x="s:-25.:-40."
                    alt="personare" class="lazy"/></a> por <a
                    href="/user/personare/history">personare</a> &nbsp; enviado: <span
                    data-ts="1509896123" class="ts visible" title="enviado: ">____</span></div>
            <div class="news-content"> Esta noche la lluvia no me ha dejado dormir. Empez&oacute; como
                si tal cosa, como algo inofensivo y sin importancia, como empiezan las cat&aacute;strofes.
                Una gota de agua cay&oacute; sobre la punta de mi nariz. Una sola, peque&ntilde;a, min&uacute;scula,
                nimia gotita. Casi me pareci&oacute; o&iacute;r el plic mientras rebotaba sobre la punta
                de mi nariz y se deslizaba hacia mi p&oacute;mulo. Abr&iacute; los ojos, pero no le di
                importancia. Creo que pens&eacute; que estaba so&ntilde;ando. Pensar que la vida es un
                sue&ntilde;o puede ser una defensa contra lo irremediable, pero es un &hellip;
            </div>
        </div>
        <div class="news-details">
            <div class="news-details-data-up"><span class="votes-up" data-toggle="tooltip"
                                                    data-placement="top" title="Votos positivos"><i
                    class="fa fa-arrow-circle-up"></i> <span
                    id="a-usu-2855636"><strong>63</strong></span></span> <span
                    class="wideonly votes-anonymous" data-toggle="tooltip" data-placement="top"
                    title="Votos anónimos"><i class="fa fa-user-secret"></i> <span
                    id="a-ano-2855636"><strong>24</strong></span></span> <span class="votes-down"
                                                                               data-toggle="tooltip"
                                                                               data-placement="top"
                                                                               title="Votos negativos"><i
                    class="fa fa-arrow-circle-down"></i> <span
                    id="a-neg-2855636"><strong>40</strong></span></span> <span class="tool karma"
                                                                               data-toggle="tooltip"
                                                                               data-placement="top"
                                                                               title="Karma"> <span
                    class="karma-letter">K</span> <span class="karma-value"
                                                        id="a-karma-2855636">  67  </span> </span> <span
                    class="tool sub-name"> <a href="/m/Artículos/queue" class="subname"
                                              style=" color:#FFFFFF !important;background-color:#0EAA74 !important; ">Artículos</a> </span>
            </div>
            <div class="news-details-main"><a class="comments"
                                              href="/story/reto-30-cuentos-5-llovio-toda-noche"
                                              title="comentarios de: «El reto de los 30 cuentos. 5.- Llovió toda la noche»">
                <i class="fa fa-comments"></i>13 comentarios </a>
                <button class="social-share"><i class="fa fa-share-alt"></i>compartir</button>
                <div class="wrapper-share-icons hide">
                    <ul class="share-icons"
                        data-url="https://www.meneame.net/story/reto-30-cuentos-5-llovio-toda-noche"
                        data-title="El reto de los 30 cuentos. 5.- Llovió toda la noche">
                        <li><a class="share-facebook" href="#" onClick="share_fb(this)"><i
                                class="fa fa-facebook-square"></i>Compartir en Facebook</a></li>
                        <li><a class="share-twitter" href="#" onClick="share_tw(this)"><i
                                class="fa fa-twitter-square"></i>Compartir en Twitter</a></li>
                        <li><a class="share-mail"
                               href="mailto:?subject=El reto de los 30 cuentos. 5.- Llovió toda la noche&body=https%3A%2F%2Fwww.meneame.net%2Fstory%2Freto-30-cuentos-5-llovio-toda-noche"
                               title="Compartir por Correo"><i class="fa fa-envelope"></i>Compartir por
                            Correo</a></li>
                        <li>
                            <button class="share-link" data-clipboard-text="http://menea.me/1p7f8"><i
                                    class="fa fa-link"></i><span>Copiar enlace</span></button>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="news-details-data-down"><span class="votes-up" data-toggle="tooltip"
                                                      data-placement="top" title="Votos positivos"><i
                    class="fa fa-arrow-circle-up"></i> <span
                    id="a-usu-2855636"><strong>63</strong></span></span> <span
                    class="wideonly votes-anonymous" data-toggle="tooltip" data-placement="top"
                    title="Votos anónimos"><i class="fa fa-user-secret"></i> <span
                    id="a-ano-2855636"><strong>24</strong></span></span> <span class="votes-down"
                                                                               data-toggle="tooltip"
                                                                               data-placement="top"
                                                                               title="Votos negativos"><i
                    class="fa fa-arrow-circle-down"></i> <span
                    id="a-neg-2855636"><strong>40</strong></span></span> <span class="tool karma"
                                                                               data-toggle="tooltip"
                                                                               data-placement="top"
                                                                               title="Karma"> <span
                    class="karma-letter">K</span> <span class="karma-value"
                                                        id="a-karma-2855636">  67  </span> </span> <span
                    class="tool sub-name"> <a href="/m/Artículos/queue" class="subname"
                                              style=" color:#FFFFFF !important;background-color:#0EAA74 !important; ">Artículos</a> </span>
            </div>
        </div>
    </div>
</div>
"""


def create_meneo(author, title, votes):
    return MENEO.format(author=author, title=title, votes=votes)


def create_page(author, title, n_meneos=10):
    meneos = [create_meneo(author='{}_{}'.format(author, meneo_i),
                           title='{}_{}'.format(title, meneo_i),
                           votes=str(meneo_i))
              for meneo_i in range(n_meneos)]

    return PAGE.format(meneos=''.join(meneos), promoted='')


@pytest.fixture(scope='session')
def valid_meneo():
    meneo_str = create_meneo(author='paco',
                             title='Ruby off the Rails',
                             votes='24')
    bs_tag = bs4.BeautifulSoup(meneo_str, "html.parser")
    meneo = Meneo(bs_tag)
    return meneo


@pytest.fixture(scope='session')
def valid_page():
    page_str = create_page(author='paco',
                           title='Ruby off the Rails',
                           n_meneos=10)
    bs_tag = bs4.BeautifulSoup(page_str, "html.parser")
    page = Page(bs_tag)
    return page


@pytest.fixture(scope='session')
def empty_page():
    page_str = create_page(author='',
                           title='',
                           n_meneos=0)
    bs_tag = bs4.BeautifulSoup(page_str, "html.parser")
    page = Page(bs_tag)
    return page


@pytest.fixture(scope='session')
def empty_page_response():
    page_str = create_page(author='',
                           title='',
                           n_meneos=0)
    return mock.MagicMock(text=page_str, spec=requests.Response)


@pytest.fixture(scope='session')
def list_of_pages(empty_page_response):
    n_pages = 10

    pages = [create_page(author='author_{}'.format(index),
                         title='title_{}'.format(index))
             for index in range(n_pages)]

    pages = [mock.MagicMock(text=page, spec=requests.Response)
            for page in pages]
    pages.append(empty_page_response)
    return pages
