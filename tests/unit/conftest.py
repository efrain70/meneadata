# -*- coding: utf-8 -*-
import pytest

import bs4

from meneadata.page.meneo import Meneo

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


@pytest.fixture()
def valid_meneo():
    meneo_str = MENEO.format(author='paco',
                             title='Ruby off the Rails',
                             votes='24')
    bs_tag = bs4.BeautifulSoup(meneo_str, "html.parser")
    meneo = Meneo(bs_tag)
    return meneo
