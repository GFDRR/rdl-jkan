---
attributions:
- entity:
    affiliation: null
    email: null
    name: Google Open Building Data
    url: https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRID3 Settlements
    url: https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas
dataset_id: rdls_exp-eth_3is_potentialsettlementexpans
description: '[Initial analysis] The database contains information about buildings
  identified by Google outside of settlements recognized by GRID3. It serves as a
  proxy for identifying potential new settlements or areas of urban growth. The analysis
  incorporates two levels of clustering: one at a distance of 500 meters and another
  at 100 meters. The 500-meter clustering helps identify broader areas where multiple
  buildings are concentrated, potentially indicating the presence of a new settlement
  or an expansion of an existing one. This distance threshold allows for the initial
  identification of potential new settlement areas. The 100-meter clustering provides
  a more granular view, highlighting tighter clusters of buildings within the broader
  500-meter areas. This finer level of clustering aids in distinguishing individual
  settlement units or neighborhoods within the larger potential settlement areas.
  By combining these two levels of clustering, the database facilitates a comprehensive
  analysis of potential new settlements or urban growth areas. It enables researchers,
  urban planners, and policymakers to identify and prioritize areas for further investigation,
  resource allocation, or development planning.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas]'
details: 'Additional Analysis Required: The dataset provides an initial indication
  of potential settlement expansion areas based on building clusters detected outside
  recognized settlements. However, further analysis is necessary to validate and confirm
  the nature and status of these areas. Additional data sources, such as high-resolution
  satellite imagery, population data, and local knowledge, should be incorporated
  to refine the analysis and ensure accurate identification of new or expanding settlements.
  Need for Remote Sensing and Ground Truthing: While the dataset relies on Google''s
  building identification, it is crucial to complement this information with remote
  sensing techniques and ground truthing efforts. High-resolution satellite imagery
  can provide valuable insights into the physical characteristics and patterns of
  the identified areas, while ground truthing through field surveys or local stakeholder
  engagement can verify the actual presence and status of potential settlements. Temporal
  Considerations: The dataset represents a snapshot in time, and settlements are dynamic
  entities that can change rapidly. Regular updates and monitoring of the identified
  areas are recommended to capture any changes or new developments in settlement patterns
  over time. Contextual Factors: The interpretation and utilization of the dataset
  should consider local contexts, including socio-economic factors, cultural practices,
  environmental conditions, and development policies. These contextual factors can
  influence settlement patterns and should be taken into account when planning interventions
  or making decisions based on the dataset. Data Limitations: It is important to acknowledge
  the potential limitations of the dataset, such as the accuracy of Google''s building
  identification algorithms, the resolution and currency of the underlying data sources,
  and any inherent biases or errors that may exist. Users should exercise caution
  and critically evaluate the dataset in conjunction with other reliable sources of
  information.'
exposure:
- asset_type:
    description: Building footprints identified by Google outside recognized settlements,
      clustered to identify potential new settlements and urban expansion areas
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints from Google's automated satellite imagery analysis
    were spatially compared against GRID3 settlement boundaries to identify structures
    outside recognized settlements. Two-level clustering analysis (500m and 100m distance
    thresholds) was applied via GIS to group isolated buildings and identify potential
    new settlement clusters and urban expansion zones.
  sources:
  - id: source_1
    license: null
    name: Google Open Building Data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: GRID3 Settlements
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-potential-settlement-expansion-areas
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
  description: Ethiopia - Potential Settlement Expansion Areas (Draft version 0.1.)
  download_url: https://data.humdata.org/dataset/43d9a671-6bea-4d46-b05e-093a6d311ea6/resource/fa43f9c0-8d5c-447e-92e6-20909d298c5e/download/eth-buildings-outside-settlements-clustered.zip
  format: null
  id: resource_fa43f9c0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ETH - Buildings outside settlements - Clustered.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eth_3is_potentialsettlementexpans
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Ethiopia - Potential Settlement Expansion Areas
version: null
vulnerability: null
---
