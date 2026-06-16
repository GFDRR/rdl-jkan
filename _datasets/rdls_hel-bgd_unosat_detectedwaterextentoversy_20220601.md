---
attributions:
- entity:
    affiliation: null
    email: null
    name: Chaohu-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2
dataset_id: rdls_hel-bgd_unosat_detectedwaterextentoversy_20220601
description: 'UNOSAT code: FL20220525BGD This map illustrates satellite-detected surface
  waters in Sylhet and Sunamganj Districts, Sylhet Division, Bangladesh as observed
  from a Chaohu-1 image acquired on 25 May 2022 at 22:23 local time. Within the analyzed
  area of about 730 km2, about 420 km2 of lands appear to be flooded. In this area,
  about 300 km2 of croplands and 70 km2 of herbaceous wetland appear to be likely
  affected by the flood waters. Based on Worldpop population data and the detected
  surface waters, about 307,000 people are potentially exposed or living close to
  flooded areas. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
    description: Croplands affected by flood waters
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Herbaceous wetland affected by flood waters
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Chaohu-1 satellite imagery acquired on 25
    May 2022 and compared it with reference imagery to detect surface water extent
    and identify flooded areas. Detected water bodies were intersected with land use
    classification (croplands, herbaceous wetland) and WorldPop population grids to
    estimate affected assets and exposed population in Sylhet and Sunamganj Districts.
  sources:
  - id: source_1
    license: null
    name: Chaohu-1 satellite imagery
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
- href: https://data.humdata.org/dataset/water-extent-over-sylhet-and-sunamganj-districts-sylhet-division-bangladesh-as-of-25-may-2
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct impact to croplands from flood inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
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
    description: Population potentially exposed to flooded areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected water extent over Sylhet and Sunamganj Districts,
    Sylhet Division, Bangladesh as of 25 May 2022. (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_gdb.zip
  format: Geodatabase
  id: resource_10c0fcf1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Sylhet and Sunamganj Districts,
    Sylhet Division, Bangladesh as of 25 May 2022. (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/BD/FL20220525BGD/FL20220525BGD_SHP.zip
  format: null
  id: resource_b5e854c1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220525BGD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_detectedwaterextentoversy_20220601
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-06-01'
temporal_resolution: null
title: Satellite detected water extent over Sylhet and Sunamganj Districts, Sylhet
  Division, Bangladesh as of 25 May 2022.
version: null
vulnerability: null
---
