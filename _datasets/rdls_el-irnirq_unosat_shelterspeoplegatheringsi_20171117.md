---
attributions:
- entity:
    affiliation: null
    email: null
    name: Airbus Defense and Space
    url: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Roscosmos
    url: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNITAR - UNOSAT
    url: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
dataset_id: rdls_el-irnirq_unosat_shelterspeoplegatheringsi_20171117
description: 'Satellite Data (1): Pleiades Imagery Dates: 16 November 2017 Resolution:
  50 cm Copyright: CNES 2017, distribution AIRBUS Defense and Space Source: Airbus
  Defense and Space Satellite Data (2): Resurs-P Imagery Dates: 14 November 2017 Resolution:1m
  Copyright: Roscosmos Source: Roscosomos Baseline Data: GADM, OpenStreetMap Analysis
  :UNITAR - UNOSAT/Iranian Space Agency Production: UNITAR - UNOSAT. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729]'
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
    description: Shelter facilities and people gathering sites identified from satellite
      imagery
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: High-resolution satellite imagery from Pleiades and Resurs-P acquired
    immediately after the 12 November 2017 Sarpol-e-Zahab earthquake was analyzed
    by UNOSAT analysts through visual interpretation and comparison with baseline
    data (GADM, OpenStreetMap) to identify and map shelter facilities and people gathering
    sites. The resulting geodatabase contains site locations, areas, confidence levels,
    and field validation status.
  sources:
  - id: source_1
    license: null
    name: Airbus Defense and Space
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Roscosmos
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: UNITAR - UNOSAT
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/shelters-and-people-gathering-sites-in-sarpol-e-zahab-kermanshah-iran-2729
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Post-earthquake assessment of shelter and gathering site locations
      and capacity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Shelters and people gathering sites in Sarpol-e-Zahab, Kermanshah,
    Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_gdb.zip
  format: Geodatabase
  id: resource_0bc7b864
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Shelters and people gathering sites in Sarpol-e-Zahab, Kermanshah,
    Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_shp.zip
  format: null
  id: resource_308c3fcd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irnirq_unosat_shelterspeoplegatheringsi_20171117
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-17'
temporal_resolution: null
title: Shelters and people gathering sites in Sarpol-e-Zahab, Kermanshah, Iran
version: null
vulnerability: null
---
