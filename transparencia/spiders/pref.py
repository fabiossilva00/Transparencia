# -*- coding: utf-8 -*-
import scrapy


class PrefSpider(scrapy.Spider):

    name = "pref"
    start_urls = ['http://www.prefeitura.sp.gov.br/cidade/secretarias/transportes/institucional/sptrans/acesso_a_informacao/index.php?p=247852']
    #n_div = 4
    #n_tr = 4
    #ultima_atualizacao = 18

    def parse(self, response):
        n_div = int(input('Digite o mes: '))
        n_tr = 1
        ultima_atualizacao = int(input('Digite o dia da ultima atualizacao: '))
        a_day = []
        while n_tr <= 5:
            divs = response.xpath('/html/body/div[1]/div[2]/article/div[2]/div/div['+str(n_div)+']/table/tbody/tr['+str(n_tr)+']/td')
            for div in divs:
                if a_day != None:
                    t_day = div.xpath('.//a/text()').extract_first()
                    a_day = div.xpath('.//a/@href').extract_first()
                    dia_atualizacao = int(t_day)
                    if dia_atualizacao > ultima_atualizacao:
                        yield {
                            'Dia': t_day,
                            'Link .xls': a_day,
                        }
            n_tr += 1

    def parse_day(self, response):
        dias = response.xpath('/html/body/div[1]/div[2]/article/div[2]/div/div['+str(n_div)+']/table/tbody/tr['+str(n_tr)+']/td')
        for dia in dias:
            last_day = dia.xpath('.//a/@href').extract_first()
        return last_day
# ('/html/body/div[1]/article/div[2]/div/div['+str(n_div)+']/table/tbody/tr['+str(n_tr)+']/td')
#                    if a_day.endswith('.xls'):
#                        yield Request(a_day, callback=self.save_xls)

#    def save_xls(self, response):
#        path = response.url.split('/')[-1]
#        with open(path, 'wb') as f:
#            f.write(response.body)
