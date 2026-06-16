---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Non-governmental organisations
    url: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
creator:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
dataset_id: rdls_exp-tcd_ochatcd_sitesdespdiscampsdesrefug
description: "Ce jeu de donn\xE9es repr\xE9sente les sites fournis par OIM, UNHCR\
  \ et les ONG qui font des \xE9valuations multi-sectorielles sur le terrain Compilation\
  \ des donn\xE9es de 2016 \xE0 aujourd'hui. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad]"
details: 'UNHCR source : https://data2.unhcr.org/en/search?country=410&country_1=0&text=&type%5B%5D=document&doc_type%5B%5D=14&partner=&working_group=&sector=&date_from=&date_to=&uploader=&country_json=%7B%220%22%3A%22410%22%7D&sector_json=%7B%220%22%3A%22%22%7D&apply='
exposure:
- asset_type:
    description: Internally displaced persons (IDPs) and refugee populations at camp
      and settlement sites
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Spatial inventory of IDP camps, refugee sites, and host villages compiled
    from direct field observations and multi-sectoral assessments conducted by UNHCR,
    IOM, and NGO partners from 2016 onwards. Data includes site locations (coordinates),
    administrative classifications, verification dates, and organizational codes for
    cross-referencing with humanitarian databases.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: IOM
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Non-governmental organisations
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sites-des-pdis-et-refugies-au-tchad
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Excel file of camps, sites, host villages for all displaced people
    (refugees, returnees, idps...) in Chad
  download_url: https://data.humdata.org/dataset/525bcfc2-e033-45b0-867c-1cf6cc1c2406/resource/1b4d4e71-273d-4d6a-b701-c65f040c54bf/download/tcd_p_hum_refugeesidps_ocha.xlsx
  format: null
  id: resource_1b4d4e71
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_p_hum_refugeesidps_ocha.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: shapefile of camps, sites, host villages for all displaced people (refugees,
    returnees, idps...) in Chad
  download_url: https://data.humdata.org/dataset/525bcfc2-e033-45b0-867c-1cf6cc1c2406/resource/6e322489-6bfb-4336-b6ee-6035adea4b94/download/tcd_p_hum_refugeesidps_ocha.zip
  format: null
  id: resource_6e322489
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tcd_p_hum_refugeesidps_ocha.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tcd_ochatcd_sitesdespdiscampsdesrefug
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: "Sites des PDIs, camps des Refugi\xE9s et villages h\xF4tes au Tchad"
version: null
vulnerability: null
---
