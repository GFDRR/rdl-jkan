---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria
dataset_id: rdls_hel-nga_unosat_detectedwaterextentsbetwe_20221019
description: "UNOSAT code FL20221019NGA This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Nigeria between 13 to 17 October 2022 compared with the period\
  \ from 08 to 12 October 2022. Within the cloud free analysed areas of about 890,000\
  \ km\xB2, a total of about 30,000 km\xB2 of land appears to be affected. In the\
  \ analysed areas, 738 health facilities and 1,424 schools are identified to be within\
  \ or close to a flooded zone. In comparison with the period between 08 to 12 October\
  \ 2022, water extent appears to have decreased of about 1,000 km\xB2. Based on Worldpop\
  \ population data and the maximal flood water extent ~6,660,000 people are potentially\
  \ exposed or living close to flooded areas amongst the 204 million people living\
  \ in the analysed zone. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria]"
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
    description: Health facilities and schools identified within or adjacent to flooded
      zones
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population exposed to flooding based on WorldPop gridded population
      data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared VIIRS satellite imagery from 13-17 October\
    \ 2022 with baseline imagery from 8-12 October 2022 to detect cumulative water\
    \ extent changes across Nigeria. Detected inundated areas (~30,000 km\xB2) were\
    \ spatially intersected with WorldPop population grids and facility registries\
    \ (health facilities and schools) to quantify exposure and affected populations."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-13-and-17-october-2022-over-nigeria
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Health facilities and schools affected by flood inundation
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood extent based on spatial overlap with
      inundated areas
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
  description: Satellite detected water extents between 13 and 17 October 2022 over
    Nigeria (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3418/FL20221019NGA_gdb.zip
  format: Geodatabase
  id: resource_06cc0d7b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 13 and 17 October 2022 over
    Nigeria (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3418/FL20221019NGA_SHP.zip
  format: null
  id: resource_aa6899e7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221019NGA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 13 and 17 October 2022 over
    Nigeria (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3418/UNOSAT_Population_Exposure_FL20221019NGA_13Oct_17Oct2022_Nigeria.xlsx
  format: null
  id: resource_54a5729b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221019NGA_13Oct_17Oct2022_Nigeria.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nga_unosat_detectedwaterextentsbetwe_20221019
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
  start: '2022-10-19'
temporal_resolution: null
title: Satellite detected water extents between 13 and 17 October 2022 over Nigeria
version: null
vulnerability: null
---
