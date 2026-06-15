---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi
dataset_id: rdls_hel-mwi_unosat_detectedwaterextentsbetwe_20230323
description: 'UNOSAT code TC20230314MWI, GDACS Id: 1000961 This map illustrates cumulative
  satellite-detected surface waters in Southern Region, Malawi between 17 to 21 March
  2023 as observed from: VIIRS imagery from 17 to 21 March 2023; Sentinel-1 imagery
  acquired on 17 Mar. 2023 and Sentinel-2 imagery acquired on 21 Mar. 2023. Within
  the analyzed area of about 30,000 km2, about 2,100 km2 of land appear to be flooded.
  Based on Worldpop population data and the detected surface waters in the analyzed
  area, ~280,000 people are potentially exposed or living close to flooded areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT). Important note:
  Flood analysis from radar images may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to the backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi]'
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
    description: Estimated population potentially exposed or living close to flooded
      areas based on WorldPop population data intersected with detected flood extents
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Multi-sensor satellite imagery (VIIRS, Sentinel-1 SAR, and Sentinel-2\
    \ optical) acquired between 17\u201321 March 2023 was analyzed by UNOSAT analysts\
    \ to delineate cumulative surface water extents across approximately 30,000 km2\
    \ of Southern Malawi following Tropical Cyclone Freddy (GDACS Id: 1000961). Detected\
    \ flood extents were spatially intersected with WorldPop population grids to estimate\
    \ the number of people potentially exposed to flooding. The resulting geodatabase\
    \ and shapefile provide flood extent polygons with sensor metadata, while the\
    \ accompanying Excel file summarizes population exposure statistics."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-17-and-21-march-2023-over-southern-region-malawi
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people (~280,000) potentially exposed to or living
      close to flooded areas in Southern Malawi during March 2023
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
  description: Satellite detected water extents between 17 and 21 March 2023 over
    Southern Region, Malawi (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3543/TC20230314MWI_gdb.zip
  format: Geodatabase
  id: resource_94cdcd7e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230314MWI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 17 and 21 March 2023 over
    Southern Region, Malawi (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3543/TC20230314MWI_SHP.zip
  format: null
  id: resource_3724af9a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230314MWI_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 17 and 21 March 2023 over
    Southern Region, Malawi (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3543/UNOSAT_Population_Exposure_TC20230314MWI_17Mar_21Mar2023_Malawi.xlsx
  format: null
  id: resource_4e13110b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230314MWI_17Mar_21Mar2023_Malawi.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mwi_unosat_detectedwaterextentsbetwe_20230323
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-23'
temporal_resolution: null
title: Satellite detected water extents between 17 and 21 March 2023 over Southern
  Region, Malawi
version: null
vulnerability: null
---
