---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: RADARSAT-2 (RCM-2)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023
dataset_id: rdls_hel-mwi_unosat_detectedwaterextentoverso_20230314
description: 'UNOSAT code TC20230314MWI, GDACS Id: 1000961 This map illustrates satellite-detected
  surface waters in Southern Region, Malawi as observed from a RCM-2 image acquired
  on 14 Mar. 2023 at 05:10 local time. Within the analyzed area of about 7,200 km2,
  about 430 km2 of land appear to be flooded. Based on Worldpop population data and
  the detected surface waters in the analyzed area, ~75,000 people are potentially
  exposed or living close to flooded areas. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to United Nations
  Satellite Centre (UNOSAT). Important note: Flood analysis from radar images may
  underestimate the presence of standing waters in built-up areas and densely vegetated
  areas due to the backscattering properties of the radar signal.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023]'
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
    description: Population potentially exposed or living close to detected flooded
      areas, derived from WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed RCM-2 satellite imagery acquired on 14 March\
    \ 2023 to detect surface water extent through visual interpretation and change\
    \ detection analysis. Detected flooded areas (~430 km\xC2\xB2) were intersected\
    \ with WorldPop gridded population data to estimate population exposure (~75,000\
    \ people) in the Southern Region of Malawi."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: RADARSAT-2 (RCM-2)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-southern-region-malawi-as-of-14-march-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flooded areas detected by satellite imagery
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
  description: Satellite detected water extent over Southern Region, Malawi as of
    14 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3529/TC20230314MWI_gdb.zip
  format: Geodatabase
  id: resource_b0dc6542
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
  description: Satellite detected water extent over Southern Region, Malawi as of
    14 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3529/TC20230314MWI_SHP.zip
  format: null
  id: resource_50129642
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
  description: Satellite detected water extent over Southern Region, Malawi as of
    14 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3529/UNOSAT_Population_Exposure_TC20230314MWI_SouthernRegion_Malawi_14Mar2023.xlsx
  format: null
  id: resource_6f214604
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230314MWI_SouthernRegion_Malawi_14Mar2023.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mwi_unosat_detectedwaterextentoverso_20230314
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
  start: '2023-03-14'
temporal_resolution: null
title: Satellite detected water extent over Southern Region, Malawi as of 14 March
  2023
version: null
vulnerability: null
---
