---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea
dataset_id: rdls_hl-dza_unosat_feuxdeforetsaunorddelalge_20170724
description: "Cette carte illustre les zones d'incendies observ\xE9es \xE0 partir\
  \ d'images satellitaires couvrant la wilaya de M\xE9d\xE9a en utilisant une diff\xE9\
  rence de ratios de br\xFBlure normalis\xE9 (NBR) d\xE9riv\xE9e des images Sentinel-2\
  \ du 29 Juin 2017 et du 19 Juillet 2017 ainsi que les foyers d'incendies d\xE9tect\xE9\
  s entre le 01 Juillet et le 19 Juillet 2017 \xE0 partir des donn\xE9es MODIS. Sur\
  \ l'emprise de cette carte, environ 5.400 ha semblent avoir brul\xE9 essentiellement\
  \ dans les communes de Ouled Bouachra (1.637 ha), Ouled Antar (1.271 ha), et Ouled\
  \ Hellal (1.134 ha). La surface totale incendi\xE9e pourrait \xEAtre sous-estim\xE9\
  e \xE9tant donn\xE9 que certaines zones semblent avoir d\xE9j\xE0 subi des incendies.\
  \ 147 foyers d'incendies ont \xE9t\xE9 d\xE9tect\xE9s durant cette p\xE9riode sur\
  \ l'\xE9tendue de la carte. Ceci est une analyse pr\xE9liminaire et n'a pas encore\
  \ \xE9t\xE9 valid\xE9e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires\
  \ \xE0 UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea]"
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
license: CC-BY-SA-4.0
lineage:
  description: "Wildfire extent was mapped by comparing Sentinel-2 satellite imagery\
    \ acquired before (29 June 2017) and after (19 July 2017) the fire event using\
    \ Normalized Burn Ratio (NBR) analysis, supplemented by MODIS thermal hotspot\
    \ detections from 1-19 July 2017. The resulting burned area polygons were validated\
    \ and quantified by commune within M\xE9d\xE9a wilaya."
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
- href: https://data.humdata.org/dataset/feux-de-forets-au-nord-de-l-algerie-impact-dans-la-wilaya-de-medea
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Direct forest area burned from wildfire in M\xE9d\xE9a wilaya, approximately\
      \ 5,400 hectares across three communes"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
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
  description: "Algeria - Feux de For\xEAts au nord de l'Alg\xE9rie - Impact dans\
    \ la wilaya de M\xE9d\xE9a (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_gdb.zip
  format: Geodatabase
  id: resource_9927ed02
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
  description: "Algeria - Feux de For\xEAts au nord de l'Alg\xE9rie - Impact dans\
    \ la wilaya de M\xE9d\xE9a (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DZ/FR20170712DZA/FR20170712DZA_SHP.zip
  format: null
  id: resource_97bea6b8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20170712DZA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dza_unosat_feuxdeforetsaunorddelalge_20170724
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
  start: '2017-07-24'
temporal_resolution: null
title: "Algeria - Feux de For\xEAts au nord de l'Alg\xE9rie - Impact dans la wilaya\
  \ de M\xE9d\xE9a"
version: null
vulnerability: null
---
