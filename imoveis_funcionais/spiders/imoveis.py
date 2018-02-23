# -*- coding: utf-8 -*-
import scrapy


class ImoveisSpider(scrapy.Spider):
    name = 'imoveis'
    start_urls = ['http://www.transparencia.gov.br/imoveisFuncionais/listaPorImovel.asp?bogus=1&Pagina=%s' % page for page in range(1,150)]


    def parse(self, response): 
        tds = response.xpath('//*[@id="listagem"]/table/tr')
        for td in tds:
            endereco = td.xpath('.//td[contains(@class, "firstChild")]/text()').extract_first()
            orgao_responsavel = td.xpath('.//td[contains(@style, "text-align: left;")]/text()').extract_first()
            situacao = td.xpath('.//td[contains(@style, "text-align: right;")]/text()').extract_first()
            
            yield {
                'endereco': endereco,
                'orgao_responsavel': orgao_responsavel,
                'situacao': situacao,
            }
