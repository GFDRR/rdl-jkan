---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec
dataset_id: rdls_hel-chl_unosat_wildfiresvinadelmarcommun_20221230
description: "UNOSAT code FR20221229CHL This map illustrates satellite-detected burned\
  \ areas in Vi\xF1a del Mar Commune, Valpara\xEDso Province, Valpara\xEDso and Metropolitan\
  \ Regions, Chile based on Sentinel-2 images acquired on 29 December 2022 at 11:52\
  \ local time. Within the map extent of about 1,700 ha, about 120 km\xB2 of lands\
  \ appear to be potentially burned. Based on Worldpop population data and the burned\
  \ area extent, about 4,000 people are potentially exposed or living close to burned\
  \ areas. This is a preliminary analysis and has not yet been validated in the field.\
  \ Please send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec]"
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
    description: Population living close to or potentially exposed to burned areas
      based on WorldPop data
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
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 29
    December 2022 and compared it with reference imagery to identify and delineate
    burned area polygons through visual interpretation. Burned area extents were then
    intersected with WorldPop gridded population data to estimate population exposure.
    This preliminary post-event damage assessment has not been validated in the field.
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-vina-del-mar-commune-valparaiso-province-valparaiso-region-chile-as-of-29-dec
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Direct land area burned by wildfire in Vi\xF1a del Mar Commune"
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
  description: "Wildfires in Vi\xF1a del Mar Commune, Valpara\xEDso Province, Valpara\xED\
    so Region, Chile as of 29 December 2022 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3469/FR20221229CHL_gdb.zip
  format: Geodatabase
  id: resource_b640523c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20221229CHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Wildfires in Vi\xF1a del Mar Commune, Valpara\xEDso Province, Valpara\xED\
    so Region, Chile as of 29 December 2022 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3469/FR20221229CHL_SHP.zip
  format: null
  id: resource_152dded9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20221229CHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chl_unosat_wildfiresvinadelmarcommun_20221230
spatial:
  bbox: null
  centroid: null
  countries:
  - CHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-12-30'
temporal_resolution: null
title: "Wildfires in Vi\xF1a del Mar Commune, Valpara\xEDso Province, Valpara\xED\
  so Region, Chile as of 29 December 2022"
version: null
vulnerability: null
---
