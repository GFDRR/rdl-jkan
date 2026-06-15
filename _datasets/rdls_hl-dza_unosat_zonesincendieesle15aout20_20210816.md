---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie
dataset_id: rdls_hl-dza_unosat_zonesincendieesle15aout20_20210816
description: "UNOSAT code: FR20210811DZA Cette carte illustre les zones incendi\xE9\
  es telles qu'observ\xE9es \xE0 partir d'une image Sentinel-2 acquise le 15 ao\xFB\
  t 2021 \xE0 10:50 UTC dans la commune d'El Amra. Sur les 22,300 ha analys\xE9s,\
  \ environ 2,500 ha de couverture v\xE9g\xE9tale/for\xEAts apparaissent comme br\xFB\
  l\xE9s. Ceci est analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e\
  \ sur le terrain. N'h\xE9sitez pas \xE0 envoyer vos commentaires au Centre Satellitaire\
  \ des Nations Unies (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie]"
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
  event_sets_by_hazard_type:
    wildfire:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 15 August 2021 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to delineate burned vegetation and forest areas. Burned zones were digitized and
    quantified by area (hectares) to produce post-event loss assessment of natural
    environment assets in El Amra commune.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zones-incendiees-le-15-aout-2021-dans-la-commune-d-el-amra-wilaya-d-ain-defla-algerie
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct vegetation and forest loss from wildfire, approximately 2,500
      ha of burned vegetation cover
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
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
  description: "Algeria - Zones incendi\xE9es le 15 ao\xFBt 2021 dans la commune d'El\
    \ Amra, wilaya d'Ain-Defla, Alg\xE9rie (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/DZ/FR20210811DZA/FR20210811DZA_gdb.zip
  format: Geodatabase
  id: resource_36a91e73
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210811DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Zones incendi\xE9es le 15 ao\xFBt 2021 dans la commune d'El\
    \ Amra, wilaya d'Ain-Defla, Alg\xE9rie (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/DZ/FR20210811DZA/FR20210811DZA_SHP.zip
  format: null
  id: resource_8125571a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210811DZA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-dza_unosat_zonesincendieesle15aout20_20210816
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
  start: '2021-08-16'
temporal_resolution: null
title: "Algeria - Zones incendi\xE9es le 15 ao\xFBt 2021 dans la commune d'El Amra,\
  \ wilaya d'Ain-Defla, Alg\xE9rie"
version: null
vulnerability: null
---
