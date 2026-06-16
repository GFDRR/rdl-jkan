---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS Earthquake Hazards Program epicentre database
    url: https://data.humdata.org/dataset/climada-earthquake-dataset
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CLIMADA (Climate Adaptation and Mitigation Project)
    url: https://data.humdata.org/dataset/climada-earthquake-dataset
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-earthquake-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-earthquake-dataset
dataset_id: rdls_hzd-ethzurich_earthquakeshazarddatadisa_1905
description: 'Earthquake hazard sets at 150 arcsec (ca. 4km) resolution, available
  for the entire globe and per country. Available as historic records from the USGS
  epicentres database and as a simple probabilistic sampling starting from the historic
  earthquake catalog, with 9 synthetic events per historic record. The presented data
  are maximum intensity on the Modified Mercalli intensity scale (MMI) over the historic
  record 1904-2017.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climada-earthquake-dataset]'
details: In this API we provide datasets in a form that can readily be used in CLIMADA
  analyses. Users should determine whether these datasets are suitable for a particular
  purpose or application, considering factors such as resolution (for example, a 4km
  grid is not suitable for modelling risk at the neighborhood level), the way that
  hazards are represented in the dataset (for example, specific events, event thresholds,
  probabilistic event sets, etc.), the way that exposure is represented, and other
  aspects. Data provided with no warranty of any kind under CC BY 4.0. See respective
  API metadata and referenced publications for details and limitations.
exposure: []
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
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Historic earthquake epicentres from the USGS database (1904-2017) were
    processed through the CLIMADA API to generate gridded maximum Modified Mercalli
    intensity (MMI) hazard data at 4km resolution. The dataset represents observed
    intensity patterns derived from the instrumental earthquake catalog, aggregated
    to administrative boundaries (admin1 level) for selected countries.
  sources:
  - id: source_1
    license: null
    name: USGS Earthquake Hazards Program epicentre database
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: CLIMADA (Climate Adaptation and Mitigation Project)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climada-earthquake-dataset
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
  url: https://github.com/CLIMADA-project/climada_petals/tree/feature/quake
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Maximum earthquake intensity over the period 1905-2017 at admin1 level
    for the HRP countries
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/dbf9b4bd-1321-4846-b6f0-4654509d3626/download/admin1-summaries-earthquake.csv
  format: null
  id: resource_dbf9b4bd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Maximum earthquake intensity by admin1 or admin2 for each earthquake
    for HRP countries
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/c0f26186-5d48-4369-a9b6-9fedda623e99/download/admin1-timeseries-summaries-earthquake.csv
  format: null
  id: resource_c0f26186
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-timeseries-summaries-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Afghanistan with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/04618b65-4dad-439f-b7c9-7dfab145be47/download/afghanistan-admin1-earthquake.csv
  format: null
  id: resource_04618b65
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Burkina Faso with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/b0b2a3bb-f337-4735-8f37-4adfb499b322/download/burkina-faso-admin1-earthquake.csv
  format: null
  id: resource_b0b2a3bb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burkina-faso-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Burundi with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/d816f779-a802-49b1-afda-f400be00ed43/download/burundi-admin1-earthquake.csv
  format: null
  id: resource_d816f779
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundi-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Cameroon with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/d4f6eed1-02f4-4aa9-b4b8-fa6f638921dd/download/cameroon-admin1-earthquake.csv
  format: null
  id: resource_d4f6eed1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cameroon-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded maximum earthquake intensity for Central African Republic with
    admin1 name column
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/8d5e0d66-2103-4ce3-9a6f-019c7bb2ef00/download/central-african-republic-admin1-earthquake.csv
  format: null
  id: resource_8d5e0d66
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: central-african-republic-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Chad with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/27507eaa-1366-42c0-9243-39c4dd0d3d74/download/chad-admin1-earthquake.csv
  format: null
  id: resource_27507eaa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: chad-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Colombia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/158110b9-25f3-4c4b-bc1f-678e4138b8ed/download/colombia-admin1-earthquake.csv
  format: null
  id: resource_158110b9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: colombia-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for DR Congo with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/c0d51e02-2065-487b-8261-ecce427b0b1b/download/dr-congo-admin1-earthquake.csv
  format: null
  id: resource_c0d51e02
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-congo-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Ethiopia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/de67ee9c-651f-413b-8af8-45aa19ae985c/download/ethiopia-admin1-earthquake.csv
  format: null
  id: resource_de67ee9c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Haiti with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/75dcbaf5-d7d5-48ce-a0e2-8450e2813cae/download/haiti-admin1-earthquake.csv
  format: null
  id: resource_75dcbaf5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Mali with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/984ac6bb-fc18-4c5b-97d4-11b0ffe40dc8/download/mali-admin1-earthquake.csv
  format: null
  id: resource_984ac6bb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mali-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Mozambique with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/63234e04-ceb5-4290-8b8b-85ad64527a02/download/mozambique-admin1-earthquake.csv
  format: null
  id: resource_63234e04
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mozambique-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Myanmar with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/45401093-802f-4caa-927d-3705d3bc2355/download/myanmar-admin1-earthquake.csv
  format: null
  id: resource_45401093
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: myanmar-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Niger with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/3c1c4419-1ab6-44dc-a83b-3a908dce7409/download/niger-admin1-earthquake.csv
  format: null
  id: resource_3c1c4419
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niger-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Nigeria with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/c66c8126-93a8-4c2f-9c62-3fe716d82aff/download/nigeria-admin1-earthquake.csv
  format: null
  id: resource_c66c8126
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Somalia with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/cb17f6dd-b08b-45c4-8d8d-a718bc98f897/download/somalia-admin1-earthquake.csv
  format: null
  id: resource_cb17f6dd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for South Sudan with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/79ffe939-a6f7-46b9-8c64-ee9c33b901ed/download/south-sudan-admin1-earthquake.csv
  format: null
  id: resource_79ffe939
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: south-sudan-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded maximum earthquake intensity for State of Palestine with admin1
    name column
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/12c2825e-eab8-48a8-ba23-56aa5a9c093a/download/state-of-palestine-admin1-earthquake.csv
  format: null
  id: resource_12c2825e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: state-of-palestine-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Sudan with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/0e213b93-9e3c-47cb-a22a-18e78ab77ddf/download/sudan-admin1-earthquake.csv
  format: null
  id: resource_0e213b93
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sudan-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded maximum earthquake intensity for Syrian Arab Republic with
    admin1 name column
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/f558dbf5-715d-4100-b96b-2608513154bf/download/syrian-arab-republic-admin1-earthquake.csv
  format: null
  id: resource_f558dbf5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syrian-arab-republic-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Ukraine with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/29976fec-7e8c-43c9-9a70-54b17a1a476f/download/ukraine-admin1-earthquake.csv
  format: null
  id: resource_29976fec
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Venezuela with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/229a25c4-4178-4a93-beb7-cdce16661b1e/download/venezuela-admin1-earthquake.csv
  format: null
  id: resource_229a25c4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: venezuela-admin1-earthquake.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)
    (Gridded maximum earthquake intensity for Yemen with admin1 name column)'
  download_url: https://data.humdata.org/dataset/744f4f0b-3172-4397-9609-5ec0b9d34fcb/resource/c4cb4c8b-3dde-49e9-b3b4-905018740b08/download/yemen-admin1-earthquake.csv
  format: null
  id: resource_c4cb4c8b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yemen-admin1-earthquake.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ethzurich_earthquakeshazarddatadisa_1905
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - PSE
  - SYR
  - VEN
  - YEM
  - AFG
  - BFA
  - BDI
  - CMR
  - CAF
  - TCD
  - COL
  - ETH
  - HTI
  - MLI
  - MOZ
  - MMR
  - NER
  - NGA
  - SOM
  - SSD
  - SDN
  - UGA
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-03'
  start: '1905-02-17'
temporal_resolution: null
title: 'Earthquakes: Hazard Data for Disaster Risk Assessment (selected countries)'
version: null
vulnerability: null
---
