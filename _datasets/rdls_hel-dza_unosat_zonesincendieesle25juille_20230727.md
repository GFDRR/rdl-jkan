---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop demographic data
    url: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie
dataset_id: rdls_hel-dza_unosat_zonesincendieesle25juille_20230727
description: "UNOSAT code FR20230724DZA, GDACS Id: 1015944 Cette carte illustre les\
  \ zones incendi\xE9es telles qu'observ\xE9es \xE0 partir d'une image Sentinel-2\
  \ acquise le 25 juillet 2023 \xE0 18:56 heure locale dans la Wilaya de Bejaia, Alg\xE9\
  rie. Sur les 540 km\xB2 de la zone observ\xE9e, environ 180 km\xB2 de v\xE9g\xE9\
  tation semblent avoir br\xFBl\xE9 dans la Wilaya de Bejaia. En se basant sur les\
  \ donn\xE9es d\xE9mographiques Worldpop, dans les communes de Semaoune, Beni Djellil\
  \ et Timzrit respectivement environ 7,200, 4,800 et 4,600 personnes sont potentiellement\
  \ impact\xE9es par les feux de for\xEAt. Ceci est une analyse pr\xE9liminaire et\
  \ n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain. Ne pas h\xE9siter \xE0 envoyer\
  \ vos commentaires au Centre Satellitaire des Nations Unies (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie]"
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
    description: Residential population in communes of Semaoune, Beni Djellil, and
      Timzrit potentially exposed to wildfire
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
- asset_type:
    description: Vegetation and forest area burned by wildfire
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts interpreted Sentinel-2 satellite imagery acquired\
    \ on 25 July 2023 to delineate wildfire burn extent in Bejaia Wilaya. Burned area\
    \ polygons were extracted and quantified (approximately 180 km\xB2 of 540 km\xB2\
    \ observed area). Population exposure was estimated by intersecting burned area\
    \ with WorldPop gridded demographic data for three communes (Semaoune, Beni Djellil,\
    \ Timzrit), yielding approximately 16,600 potentially affected persons."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop demographic data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zones-incendiees-le-25-juillet-2023-dans-la-wilaya-de-bejaia-algerie
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially impacted by wildfire in three communes based
      on burned area extent and demographic data
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: "Vegetation and forest area destroyed by wildfire (approximately\
      \ 180 km\xB2 burned)"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: wildfire
    id: loss_2
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
  description: "Algeria - Zones incendi\xE9es le 25 juillet 2023 dans la Wilaya de\
    \ Bejaia, Alg\xE9rie (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3644/FR20230724DZA_gdb.zip
  format: Geodatabase
  id: resource_9724da17
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
  description: "Algeria - Zones incendi\xE9es le 25 juillet 2023 dans la Wilaya de\
    \ Bejaia, Alg\xE9rie (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3644/FR20230724DZA_SHP.zip
  format: null
  id: resource_c0e84176
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Zones incendi\xE9es le 25 juillet 2023 dans la Wilaya de\
    \ Bejaia, Alg\xE9rie (Excel file)"
  download_url: https://unosat.org/static/unosat_filesystem/3644/UNOSAT_PopulationExposed_BurnedArea_Bejaia_FR20230724DZA_25072023.xlsx
  format: null
  id: resource_89336cbe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposed_BurnedArea_Bejaia_FR20230724DZA_25072023.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-dza_unosat_zonesincendieesle25juille_20230727
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
  start: '2023-07-27'
temporal_resolution: null
title: "Algeria - Zones incendi\xE9es le 25 juillet 2023 dans la Wilaya de Bejaia,\
  \ Alg\xE9rie"
version: null
vulnerability: null
---
