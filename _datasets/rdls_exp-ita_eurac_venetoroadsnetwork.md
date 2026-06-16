---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
creator:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
dataset_id: rdls_exp-ita_eurac_venetoroadsnetwork
description: 'Rete stradale derivata da DataBase strati prioritario in scala 1:10.000
  (Regione Veneto,Sezione Pianificazione Territoriale Strategica e Cartografia) [Source:
  This metadata record was automatically extracted from the GeoNode portal eurac]'
details: 'Full metadata document: https://idt2.regione.veneto.it/geoportal/catalog/search/resource/details.page?uuid=r_veneto:c01070240012_ElementoStradale'
exposure:
- asset_type: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: "(4m accuracy) Storia del dato: Carta Tecnica Regionale, rete stradale\
    \ di interesse regionale (BD mobilit\u221A\u2020 in scala 1:50.000). - Estrazione\
    \ dalla CTR dei tratti stradali. Digitalizzazione dove non presente in CTR. Controllo\
    \ della corretta convergenza dei tratti nei nodi. Ad ogni tratto sono stati assegnati\
    \ gli attributi specifici."
  sources:
  - id: source_1
    license: null
    name: Piero Campalani
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/771
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Authoritative dataset of roads in Veneto, Italy.
referenced_by: []
resources:
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:veneto_tran_rds_ln_s4_pa_pp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (OGC WMS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:veneto_tran_rds_ln_s4_pa_pp&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:veneto_tran_rds_ln_s4_pa_pp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (OGC WFS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:veneto_tran_rds_ln_s4_pa_pp&outputFormat=application%2Fjson
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (Zipped Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=SHAPE-ZIP&srs=EPSG%3A3003&format_options=charset%3AUTF-8
  format: null
  id: resource_2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=gml2&srs=EPSG%3A3003
  format: null
  id: resource_3
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A3003
  format: null
  id: resource_4
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=csv&srs=EPSG%3A3003
  format: null
  id: resource_5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=excel&srs=EPSG%3A3003
  format: null
  id: resource_6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3003
  description: 'Veneto: Roads Network (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Aveneto_tran_rds_ln_s4_pa_pp&outputFormat=json&srs=EPSG%3A3003&srsName=EPSG%3A3003
  format: null
  id: resource_7
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ita_eurac_venetoroadsnetwork
spatial:
  bbox:
  - 1626111.375
  - 4964936.0
  - 1818502.0
  - 5166798.5
  centroid: null
  countries:
  - ITA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2011'
temporal_resolution: null
title: 'Veneto: Roads Network'
version: null
vulnerability: null
---
