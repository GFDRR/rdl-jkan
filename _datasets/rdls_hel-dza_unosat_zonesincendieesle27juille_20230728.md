---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Pl\xE9iades satellite imagery"
    url: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas
dataset_id: rdls_hel-dza_unosat_zonesincendieesle27juille_20230728
description: "UNOSAT code FR20230724DZA, GDACS Id: 1015944 Cette carte illustre les\
  \ zones incendi\xE9es telles qu'observ\xE9es \xE0 partir d'une image Pl\xE9iades\
  \ acquise le 27 juillet 2023 \xE0 11:21 heure locale dans les communes de Melbou\
  \ et Mansouria. Sur les 70 km\xB2 de la zone observ\xE9e, environ 15km\xB2 et 8m\xB2\
  \ de v\xE9g\xE9tation semblent avoir br\xFBl\xE9 dans les communes de Melbou et\
  \ Ziama Mansouria. En se basant sur les donn\xE9es d\xE9mographiques Worldpop, dans\
  \ les communes de Melbou et Ziama Mansouria respectivement environ 2,600 et 5,000\
  \ personnes sont potentiellement impact\xE9es par les feux de for\xEAt. Ceci est\
  \ une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Ne pas h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire des Nations\
  \ Unies (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Vegetation area burned in wildfire event
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Residential population potentially impacted by wildfire in affected
      communes
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
  type: wildfire
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts interpreted Pl\xE9iades satellite imagery acquired\
    \ 27 July 2023 to delineate wildfire-burned areas in two Algerian communes. Burned\
    \ vegetation extent was digitized and quantified (approximately 23 km\xB2 total).\
    \ WorldPop gridded population data was overlaid to estimate potentially affected\
    \ population (approximately 7,600 persons combined). Results were delivered as\
    \ vector geodatabase and shapefile formats."
  sources:
  - id: source_1
    license: null
    name: "Pl\xE9iades satellite imagery"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zones-incendiees-le-27-juillet-2023-dans-les-communes-de-melbou-et-ziama-mansouria-wilayas
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Direct vegetation loss from wildfire with approximately 23 km\xB2\
      \ burned area"
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
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by wildfire in Melbou and Ziama Mansouria
      communes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: "Algeria - Zones incendi\xE9es le 27 juillet 2023 dans les communes\
    \ de Melbou et Ziama Mansouria, Wilayas de Bejaia et Jijel, Alg\xE9rie (Zipped\
    \ geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3646/FR20230724DZA_gdb.zip
  format: Geodatabase
  id: resource_4e90f36a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Zones incendi\xE9es le 27 juillet 2023 dans les communes\
    \ de Melbou et Ziama Mansouria, Wilayas de Bejaia et Jijel, Alg\xE9rie (Zipped\
    \ shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3646/FR20230724DZA_SHP.zip
  format: null
  id: resource_6f285de0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-dza_unosat_zonesincendieesle27juille_20230728
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
  start: '2023-07-28'
temporal_resolution: null
title: "Algeria - Zones incendi\xE9es le 27 juillet 2023 dans les communes de Melbou\
  \ et Ziama Mansouria, Wilayas de Bejaia et Jijel, Alg\xE9rie"
version: null
vulnerability: null
---
