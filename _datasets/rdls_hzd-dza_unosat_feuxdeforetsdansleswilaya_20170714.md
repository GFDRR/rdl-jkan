---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie
dataset_id: rdls_hzd-dza_unosat_feuxdeforetsdansleswilaya_20170714
description: "Cette carte illustre les zones d'incendies observ\xE9es \xE0 partir\
  \ d'images satellites Sentinel-2 couvrant des secteurs des wilayas de Tizi Ouzou\
  \ et Boumerd\xE8s en utilisant une diff\xE9rence de ratios de br\xFBlure normalis\xE9\
  \ (NBR) d\xE9riv\xE9e des images Sentinel-2 du 29 Juin 2017 et du 09 Juillet 2017\
  \ ainsi que les foyers d'incendies d\xE9tect\xE9s entre le 01 Juillet et le 13 Juillet\
  \ 2017 \xE0 partir des donn\xE9es MODIS. Sur l'emprise de cette carte, environ 113ha\
  \ de zones v\xE9g\xE9talis\xE9es semblent br\xFBl\xE9es principalement des zones\
  \ foresti\xE8res. 35 foyers incendi\xE9s ont \xE9t\xE9 d\xE9tect\xE9s durant cette\
  \ p\xE9riode. Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9\
  e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires \xE0 UNITAR-UNOSAT..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie]"
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
  - analysis_type: probabilistic
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
  type: wildfire
license: CC-BY-SA-4.0
lineage:
  description: Wildfire extent and hotspot data were derived from multi-temporal Sentinel-2
    satellite imagery (29 June - 9 July 2017) using normalized burn ratio (NBR) differencing
    to delineate burned areas (~113 ha), combined with MODIS thermal anomaly detection
    (1-13 July 2017) to identify active fire locations. UNOSAT analysts manually reviewed
    and validated satellite imagery changes to produce post-event wildfire mapping
    for disaster assessment in northern Algeria.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/feux-de-forets-dans-les-wilayas-boumerdes-et-tizi-ouzou-algerie
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
  description: "Algeria - Feux de For\xEAts dans les Wilayas Boumerd\xE8s et Tizi\
    \ Ouzou, Alg\xE9rie (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_df748dfb
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
  description: "Algeria - Feux de For\xEAts dans les Wilayas Boumerd\xE8s et Tizi\
    \ Ouzou, Alg\xE9rie (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_341d1b41
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
slug: rdls_hzd-dza_unosat_feuxdeforetsdansleswilaya_20170714
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
  start: '2017-07-14'
temporal_resolution: null
title: "Algeria - Feux de For\xEAts dans les Wilayas Boumerd\xE8s et Tizi Ouzou, Alg\xE9\
  rie"
version: null
vulnerability: null
---
