---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-between-18-and-22-september-2024-over-far-north-region-cameroon
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-18-and-22-september-2024-over-far-north-region-cameroon
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-18-and-22-september-2024-over-far-north-region-cameroon
dataset_id: rdls_he-cmr_unosat_detectedwaterextentsbetwe_20240923
description: "UNOSAT code: FL20240821CMR This map illustrates cumulative satellite-detected\
  \ water extent in Farth-North Region, Cameroon between 18 to 22 September 2024.\
  \ Within the cloud free analysed areas of about 34,000 km\xB2, a total of about\
  \ 6,000 km\xB2 of lands appear to be affected with flood waters. Water extent appears\
  \ to have increased of about 1,800 km\xB2 since the period between 16 to 20 August\
  \ 2024. Based on Worldpop population data and the maximum flood water extent, ~415,000\
  \ people in Far-North Region are potentially exposed or living close to flooded\
  \ areas, amongst which ~270,000 people in Logone-et-Chari Department and ~125,000\
  \ people in Mayo-Danay Department. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-18-and-22-september-2024-over-far-north-region-cameroon]"
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
    description: Population potentially exposed to or living close to flooded areas,
      estimated at approximately 415,000 people based on WorldPop data and maximum
      flood extent
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Satellite imagery from multiple sensors was analyzed by UNOSAT analysts
    comparing images from 18-22 September 2024 to detect changes in water extent.
    The maximum flood water extent polygon was overlaid with WorldPop population data
    to estimate exposure. Results are provided as vector geometries (shapefile, geodatabase)
    and tabular population exposure statistics.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/water-extents-between-18-and-22-september-2024-over-far-north-region-cameroon
  rel: source
loss: null
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
  description: Satellite detected water extents between 18 and 22 September 2024 over
    Far-North Region, Cameroon (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3979/FL20240821CMR_gdb.zip
  format: Geodatabase
  id: resource_91601ec9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240821CMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 18 and 22 September 2024 over
    Far-North Region, Cameroon (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3979/FL20240821CMR_SHP.zip
  format: null
  id: resource_472eb5f2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240821CMR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 18 and 22 September 2024 over
    Far-North Region, Cameroon (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3979/UNOSAT_Population_Exposure_FL20240821CMR_18Sep_22Sep2024_CMR.xlsx
  format: null
  id: resource_5793e22c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240821CMR_18Sep_22Sep2024_CMR.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cmr_unosat_detectedwaterextentsbetwe_20240923
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-23'
temporal_resolution: null
title: Satellite detected water extents between 18 and 22 September 2024 over Far-North
  Region, Cameroon
version: null
vulnerability: null
---
