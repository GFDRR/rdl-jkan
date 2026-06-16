---
attributions:
- entity:
    affiliation: null
    email: null
    name: ETH Zurich Climada
    url: https://data.humdata.org/dataset/climada-litpop-dataset
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-litpop-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-litpop-dataset
dataset_id: rdls_exp-codpsesyrvenyem_ethzurich_litpophumanitarianrespons_2020
description: 'A high-resolution asset exposure dataset produced using ''lit population''
  (LitPop), a globally consistent methodology to disaggregate asset value data proportional
  to a combination of nightlight intensity and geographical population data. Exposure
  data for population, asset values and productive capital at 4km spatial resolution
  globally, consistent across country borders. The dataset offers value for manifold
  use cases, including globally consistent economic disaster risk assessments and
  climate change adaptation studies, especially for larger regions, yet at considerably
  high resolution. The Climada Data API can be used to explore the full, original
  datasets.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climada-litpop-dataset]'
details: '2024-01-10: There is an issue with the Syria data so it is not included,
  this issue is being addressed In this API we provide datasets in a form that can
  readily be used in CLIMADA analyses. Users should determine whether these datasets
  are suitable for a particular purpose or application, considering factors such as
  resolution (for example, a 4km grid is not suitable for modelling risk at the neighborhood
  level), the way that hazards are represented in the dataset (for example, specific
  events, event thresholds, probabilistic event sets, etc.), the way that exposure
  is represented, and other aspects. Data provided with no warranty of any kind under
  CC BY 4.0. See respective API metadata and referenced publications for details and
  limitations.'
exposure:
- asset_type:
    description: Gridded population distribution disaggregated to 4km resolution using
      nightlight intensity and census data
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
      quantity_kind: currency
      unit: null
- asset_type:
    description: Asset values and productive capital disaggregated to 4km resolution
      using LitPop methodology
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Asset exposure data generated using the LitPop methodology, which disaggregates
    national asset value data proportional to a combination of nightlight intensity
    and geographical population data at 4km spatial resolution. The dataset integrates
    nightlight satellite imagery with census population data to produce globally consistent
    economic exposure estimates suitable for disaster risk assessment and climate
    adaptation studies.
  sources:
  - id: source_1
    license: null
    name: ETH Zurich Climada
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climada-litpop-dataset
  rel: source
loss: null
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
  url: https://doi.org/10.5194/essd-12-817-2020
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://doi.org/10.3929/ethz-b-000331316
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Summed LitPop data at admin1 level for the HRP countries)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/96b24403-0de4-4652-bb76-f585c04b5e6d/download/admin1-summaries-litpop.csv
  format: null
  id: resource_96b24403
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Afghanistan with admin1 name
    column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/1aeaf470-2e38-4a6b-a704-3c5ff2fd7c02/download/afghanistan-admin1-litpop.csv
  format: null
  id: resource_1aeaf470
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Burkina Faso with admin1 name
    column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/7bd5d7a5-5537-46bd-9a99-7184fd1316ed/download/burkina-faso-admin1-litpop.csv
  format: null
  id: resource_7bd5d7a5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burkina-faso-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Burundi with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/d9d8507d-e0b9-45cc-8be1-10cadde01ba0/download/burundi-admin1-litpop.csv
  format: null
  id: resource_d9d8507d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundi-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Cameroon with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/670a9a1e-f685-4d9e-ac30-c8555afdac5e/download/cameroon-admin1-litpop.csv
  format: null
  id: resource_670a9a1e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cameroon-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Central African Republic with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/6efb07f0-c1a4-4cbd-bdc6-eceb8d503a70/download/central-african-republic-admin1-litpop.csv
  format: null
  id: resource_6efb07f0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: central-african-republic-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Chad with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/b705103c-3057-415b-919f-a41b679cd1a5/download/chad-admin1-litpop.csv
  format: null
  id: resource_b705103c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: chad-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Colombia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/41f3fef4-7081-4309-bf3d-f7ed5ab52345/download/colombia-admin1-litpop.csv
  format: null
  id: resource_41f3fef4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: colombia-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for DR Congo with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/2f137b88-a951-4535-a214-499d7fbe0b61/download/dr-congo-admin1-litpop.csv
  format: null
  id: resource_2f137b88
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-congo-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Ethiopia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/561fc205-ad4d-44c6-b25d-7369d205848b/download/ethiopia-admin1-litpop.csv
  format: null
  id: resource_561fc205
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Haiti with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/2d3c933d-1fa0-4689-b383-83c519dc2852/download/haiti-admin1-litpop.csv
  format: null
  id: resource_2d3c933d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Mali with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/dadac817-5538-44f2-81b8-8f71691b8eac/download/mali-admin1-litpop.csv
  format: null
  id: resource_dadac817
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mali-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Mozambique with admin1 name
    column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/7a47f888-be3c-491d-a6bc-25b74a4d24e5/download/mozambique-admin1-litpop.csv
  format: null
  id: resource_7a47f888
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mozambique-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Myanmar with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/1b105002-cf1d-4345-ba32-02c720d5e728/download/myanmar-admin1-litpop.csv
  format: null
  id: resource_1b105002
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: myanmar-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Niger with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/33245f82-299e-486c-8080-3545e19a4cd5/download/niger-admin1-litpop.csv
  format: null
  id: resource_33245f82
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niger-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Nigeria with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/26a5c0d6-53b0-45e9-86d5-ee319caf10e0/download/nigeria-admin1-litpop.csv
  format: null
  id: resource_26a5c0d6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Somalia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/a8c602ab-ec6c-4c2c-af7f-3eaa05f3cb0d/download/somalia-admin1-litpop.csv
  format: null
  id: resource_a8c602ab
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for South Sudan with admin1 name
    column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/8f36d62b-5067-44f4-845f-c9508d7894d9/download/south-sudan-admin1-litpop.csv
  format: null
  id: resource_8f36d62b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: south-sudan-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for State of Palestine with admin1
    name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/ce199a9d-4bad-4ecd-8cf6-f13b094ae4e8/download/state-of-palestine-admin1-litpop.csv
  format: null
  id: resource_ce199a9d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: state-of-palestine-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Sudan with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/42647164-5624-45e8-8478-4005b396a3fc/download/sudan-admin1-litpop.csv
  format: null
  id: resource_42647164
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sudan-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Ukraine with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/fff16413-41d5-4dcd-9875-d8433fcbfd57/download/ukraine-admin1-litpop.csv
  format: null
  id: resource_fff16413
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Venezuela with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/b31ea722-0bf6-4056-9fc1-ec72e16cf01f/download/venezuela-admin1-litpop.csv
  format: null
  id: resource_b31ea722
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: venezuela-admin1-litpop.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for
    Disaster Risk Assessment (Gridded LitPop data for Yemen with admin1 name column)'
  download_url: https://data.humdata.org/dataset/3527869c-8fe9-4289-9d57-1811e789bf60/resource/9a508cd0-3bd4-4241-9196-e4a4a119d31d/download/yemen-admin1-litpop.csv
  format: null
  id: resource_9a508cd0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yemen-admin1-litpop.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-codpsesyrvenyem_ethzurich_litpophumanitarianrespons_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - PSE
  - SYR
  - VEN
  - YEM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: 'LitPop: Humanitarian Response Plan (HRP) Countries Exposure Data for Disaster
  Risk Assessment'
version: null
vulnerability: null
---
