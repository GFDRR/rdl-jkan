---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica
dataset_id: rdls_hel-nic_unosat_detectedwaterextentsbetwe_20221018
description: "UNOSAT code TC20221014NIC This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Region Autonoma del Atlantico Norte, Nicaragua between 12\
  \ to 16 October 2022 compared with the period from 27 September to 01 October 2022.\
  \ Within the cloud free analyzed areas of about 30,000 km\xB2, a total of about\
  \ 1,900 km\xB2 of lands appear to be affected. Water extent appears to have increased\
  \ of about 1,400 km\xB2 since the period between 27 September to 01 October 2022.\
  \ Based on Worldpop population data and the maximal flood water extent ~8,500 people\
  \ are potentially exposed or living close to flooded areas amongst the 29,000 people\
  \ living in cloud free areas. This is a preliminary analysis and has not yet been\
  \ validated in the field. Please send ground feedback to the United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica]"
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
    description: Population potentially exposed to flood water extent based on WorldPop
      data overlay
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared VIIRS satellite imagery from 12-16 October\
    \ 2022 with baseline imagery from 27 September-1 October 2022 to detect cumulative\
    \ water extent changes. Water extent polygons were delineated through visual interpretation\
    \ of cloud-free areas (~30,000 km\xB2). Population exposure was estimated by overlaying\
    \ the maximal flood extent with WorldPop gridded population data to derive affected\
    \ population counts."
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
- href: https://data.humdata.org/dataset/water-extents-between-12-and-16-october-2022-over-region-autonoma-del-atlantico-norte-nica
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by observed flood water extent during October
      2022 event
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
  description: Satellite detected water extents between 12 and 16 October 2022 over
    Region Autonoma del Atlantico Norte, Nicaragua (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3411/TC20221014NIC_gdb.zip
  format: Geodatabase
  id: resource_eca3b20e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221014NIC_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 12 and 16 October 2022 over
    Region Autonoma del Atlantico Norte, Nicaragua (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3411/TC20221014NIC_SHP.zip
  format: null
  id: resource_cf912fce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20221014NIC_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nic_unosat_detectedwaterextentsbetwe_20221018
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-18'
temporal_resolution: null
title: Satellite detected water extents between 12 and 16 October 2022 over Region
  Autonoma del Atlantico Norte, Nicaragua
version: null
vulnerability: null
---
