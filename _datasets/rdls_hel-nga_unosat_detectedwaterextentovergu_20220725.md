---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022
dataset_id: rdls_hel-nga_unosat_detectedwaterextentovergu_20220725
description: 'UNOSAT code: FL20220721NGA This map illustrates satellite-detected surface
  waters in Gujba LGA, Yobe state, Nigeria as observed from a Sentinel-1 image acquired
  on 18 Jul 2022 at 18:22 local time. Within the analyzed area of about 1,040 km2,
  about 22 km2 of lands appear to be flooded. Based on Worldpop population data and
  the detected surface waters, about 1,400 people are potentially exposed or living
  within/close to flooded areas. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT). Important note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022]'
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
    description: Population potentially exposed or living within/close to flooded
      areas based on WorldPop data
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts performed change detection analysis on Sentinel-1\
    \ SAR imagery acquired 18 Jul 2022 to identify surface water extent in Gujba LGA.\
    \ Detected water bodies (22 km\xB2 within 1,040 km\xB2 study area) were intersected\
    \ with WorldPop gridded population data to estimate approximately 1,400 people\
    \ potentially exposed to flooding. This is a preliminary post-event satellite-based\
    \ assessment not yet validated in the field."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-gujba-lga-yobe-state-nigeria-as-of-18-jul-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by detected surface water inundation from satellite
      imagery
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
  description: Satellite detected water extent over Gujba LGA, Yobe state, Nigeria
    as of 18 Jul 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/NG/FL20220721NGA/FL20220721NGA_gdb.zip
  format: Geodatabase
  id: resource_e69136dc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220721NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Gujba LGA, Yobe state, Nigeria
    as of 18 Jul 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/NG/FL20220721NGA/FL20220721NGA_shp.zip
  format: null
  id: resource_0f9eef0b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220721NGA_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nga_unosat_detectedwaterextentovergu_20220725
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-07-25'
temporal_resolution: null
title: Satellite detected water extent over Gujba LGA, Yobe state, Nigeria as of 18
  Jul 2022
version: null
vulnerability: null
---
