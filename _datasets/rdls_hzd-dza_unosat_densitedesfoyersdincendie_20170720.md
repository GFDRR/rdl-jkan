---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017
dataset_id: rdls_hzd-dza_unosat_densitedesfoyersdincendie_20170720
description: "Cette carte illustre la densit\xE9 des foyers d'incendies d\xE9tect\xE9\
  s \xE0 partir des donn\xE9es MODIS de la NASA, accessible via NASA FIRMS avec une\
  \ r\xE9solution de 1 km, dans le nord de l'Alg\xE9rie entre le 17 et le 19 juillet\
  \ 2017. 54 foyers ont \xE9t\xE9 d\xE9tect\xE9s durant cette p\xE9riode alors que\
  \ pour la p\xE9riode allant du 14 au 16 juillet leur nombre s'\xE9levait \xE0 99.\
  \ Cette carte confirme une tendance \xE0 la baisse du nombre de foyers d'incendies\
  \ sur cette p\xE9riode. Les aper\xE7us illustrent des zones incendi\xE9es observ\xE9\
  es \xE0 partir d'images satellitaires, Alsat-2B du 06 juillet 2017 sur une zone\
  \ \xE0 l'est de Tamalous (W. de Skikda) et Landsat-8 acquises le 25 juin et le 11\
  \ juillet 2017 couvrant les massifs situ\xE9s \xE0 la limite des wilayas de Jijel\
  \ et de Bejaia. Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9\
  \ valid\xE9e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires \xE0\
  \ UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Active fire hotspots were detected from NASA MODIS satellite data via
    the FIRMS system at 1 km resolution for the period 17-19 July 2017 in northern
    Algeria. UNOSAT analysts processed these detections to generate a density map
    showing spatial concentration of fire locations, with supporting validation from
    Alsat-2B satellite imagery acquired on 6 July 2017.
  sources:
  - id: source_1
    license: null
    name: NASA FIRMS (Fire Information for Resource Management System)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-au-nord-de-l-algerie-entre-le-17-et-le-19-juillet-2017
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies au nord de l'Alg\xE9rie\
    \ entre le 17 et le 19 juillet 2017 (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_7da7de4c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies au nord de l'Alg\xE9rie\
    \ entre le 17 et le 19 juillet 2017 (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_02409eb0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-dza_unosat_densitedesfoyersdincendie_20170720
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-07-20'
temporal_resolution: null
title: "Algeria - Densit\xE9 des foyers d'incendies au nord de l'Alg\xE9rie entre\
  \ le 17 et le 19 juillet 2017"
version: null
vulnerability: null
---
