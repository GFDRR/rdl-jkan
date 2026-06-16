---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldView-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022
dataset_id: rdls_hel-tcd_unosat_detectedwaterextentndjame_20221027
description: 'UNOSAT code FL20221019TCD This map illustrates satellite-detected surface
  waters in N''Djamena Department, N''Djamena Region, Chad as observed from a WorldView-2
  image acquired on 24 October 2022 at 10:38 local time. Within the analyzed area
  of about 300 km2, about 38 km2 of lands appear to be flooded and 14,799 structures
  are potentially affected by the floods. Based on Worldpop population data and the
  detected surface waters, about 154,000 people are potentially exposed or living
  close to flooded areas. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022]'
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
    description: Building structures potentially affected by detected flood waters
      in N'Djamena Department
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed WorldView-2 satellite imagery acquired on\
    \ 24 October 2022 and performed visual change detection to identify surface water\
    \ extent in N'Djamena Department. Detected flood polygons (38 km\xC2\xB2 inundated\
    \ area) were intersected with building footprints and WorldPop population grids\
    \ to estimate structural and population exposure to the observed flooding event."
  sources:
  - id: source_1
    license: null
    name: WorldView-2 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extent-in-n-djamena-department-n-djamena-region-chad-as-of-24-october-2022
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building structures potentially affected by satellite-detected flood
      waters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooded areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Satellite detected water extent in N'Djamena department, N'Djamena
    Region, Chad as of 24 October 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3428/FL20221019TCD_gdb.zip
  format: Geodatabase
  id: resource_df4a0edb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in N'Djamena department, N'Djamena
    Region, Chad as of 24 October 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3428/FL20221019TCD_SHP.zip
  format: null
  id: resource_3cdc50bb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019TCD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-tcd_unosat_detectedwaterextentndjame_20221027
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-27'
temporal_resolution: null
title: Satellite detected water extent in N'Djamena department, N'Djamena Region,
  Chad as of 24 October 2022
version: null
vulnerability: null
---
