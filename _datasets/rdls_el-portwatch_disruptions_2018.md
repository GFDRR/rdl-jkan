---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Disaster Alert and Coordination System (GDACS)
    url: https://data.humdata.org/dataset/disruptions
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: PortWatch ports and chokepoints database
    url: https://data.humdata.org/dataset/disruptions
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: PortWatch
  url: https://data.humdata.org/dataset/disruptions
creator:
  affiliation: null
  email: null
  name: PortWatch
  url: https://data.humdata.org/dataset/disruptions
dataset_id: rdls_el-portwatch_disruptions_2018
description: 'The PortWatch Disruptions dataset collects data from the Global Disaster
  Alert and Coordination System ( GDACS ), which provides alerts on natural hazards
  such as earthquakes, tsunamis, tropical cyclones, floods, volcanic eruptions, and
  droughts, as well as other types of disruptions such as those arising from geopolitical
  tensions. PortWatch intersects this data with their ports and chokepoints databases
  to identify locations that may be at risk of being disrupted.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/disruptions]'
details: The API is queried every Tuesday. If new data is available, the dataset is
  automatically updated.
exposure:
- asset_type:
    description: Port facilities and maritime chokepoints at risk of disruption
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
    description: Affected population in areas with disrupted ports
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
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset integrates real-time hazard alerts from GDACS with PortWatch's
    spatial database of global ports and maritime chokepoints to identify port disruption
    events. GDACS alerts are intersected with port locations to determine affected
    facilities and associated populations, creating a disruption event record with
    severity classification and temporal coverage.
  sources:
  - id: source_1
    license: null
    name: Global Disaster Alert and Coordination System (GDACS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: PortWatch ports and chokepoints database
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disruptions
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from earthquake events
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
        metric: disruption
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from tsunami events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: disruption
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from tropical cyclone events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: disruption
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: disruption
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from volcanic eruption events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: disruption
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Port disruption from drought events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: disruption
        modelling: observed
        type: indirect
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.imf.org/en/publications/wp/issues/2021/08/20/tracking-trade-from-space-an-application-to-pacific-island-countries-464345
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://www.imf.org/en/publications/wp/issues/2025/05/16/nowcasting-global-trade-from-space-566957
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset identifying ports and chokepoints at risk by intersecting GDACS
    data. See variable descriptions here
  download_url: https://data.humdata.org/dataset/c23fcd1f-117b-4ce0-8304-d14896e8ffad/resource/84642cfa-6fb6-4648-8b37-1d9db5aa184b/download/disruptions.csv
  format: null
  id: resource_84642cfa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disruptions.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset in GeoJSON format identifying ports and chokepoints at risk
    by intersecting GDACS data. See variable descriptions here
  download_url: https://data.humdata.org/dataset/c23fcd1f-117b-4ce0-8304-d14896e8ffad/resource/af35f4e2-0778-48e7-8af7-1743e1f65e13/download/disruptions.geojson
  format: null
  id: resource_af35f4e2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disruptions.geojson
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-portwatch_disruptions_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-11'
  start: '2018-10-21'
temporal_resolution: null
title: Disruptions
version: null
vulnerability: null
---
