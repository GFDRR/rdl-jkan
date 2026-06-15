---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS (Moderate Resolution Imaging Spectroradiometer)
    url: https://data.humdata.org/dataset/climada-wildfire-dataset
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ETH Zurich Climada
    url: https://data.humdata.org/dataset/climada-wildfire-dataset
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-wildfire-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-wildfire-dataset
dataset_id: rdls_hzd-ethzurich_wildfirehumanitarianrespo_2001
description: 'Global wildfire dataset at 4km resolution, based on MODIS satellite
  data 2000-2021 (cf https://firms.modaps.eosdis.nasa.gov).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/climada-wildfire-dataset]'
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
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "MODIS satellite fire detection data from NASA FIRMS (2000-2021) was\
    \ processed through the Climada v2.2 API to generate globally consistent wildfire\
    \ hazard metrics aggregated at 4km resolution and summarized by administrative\
    \ boundaries for HRP countries, following the methodology described in L\xFCthi\
    \ et al. (2021)."
  sources:
  - id: source_1
    license: null
    name: MODIS (Moderate Resolution Imaging Spectroradiometer)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: ETH Zurich Climada
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climada-wildfire-dataset
  rel: source
loss:
  losses: []
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
  url: https://gmd.copernicus.org/articles/14/7175/2021/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Wildfire extent over the period 2001-2021 at admin1
    level for the HRP countries)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/3bedc412-c936-4b2f-9b1b-a53700c2e211/download/admin1-summaries-wildfire.csv
  format: null
  id: resource_3bedc412
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Wildfire extent by admin1 or admin2 for each fire for
    HRP countries)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/37df8513-6859-464e-a1cc-e83bf2e2fb36/download/admin1-timeseries-summaries-wildfire.csv
  format: null
  id: resource_37df8513
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-timeseries-summaries-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Afghanistan at
    with admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/96599799-f37b-4ab2-bc1b-643de3e60fc1/download/afghanistan-admin1-wildfire.csv
  format: null
  id: resource_96599799
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Burkina Faso at
    with admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/7c05f270-c131-48a2-9aaf-7867c933cae3/download/burkina-faso-admin1-wildfire.csv
  format: null
  id: resource_7c05f270
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burkina-faso-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Burundi at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/a2b5171a-69a1-49a4-aafc-290c34cb99c9/download/burundi-admin1-wildfire.csv
  format: null
  id: resource_a2b5171a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundi-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Cameroon at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/6ff41dda-de39-4382-9670-3501ecd159fa/download/cameroon-admin1-wildfire.csv
  format: null
  id: resource_6ff41dda
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cameroon-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) wildfire extent for Central African Republic at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/77bcdd6c-2667-4894-82cd-628ee9782e36/download/central-african-republic-admin1-wildfire.csv
  format: null
  id: resource_77bcdd6c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: central-african-republic-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Chad at with admin1
    name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/0a30b364-a9fb-4a4b-b21d-c161254b4344/download/chad-admin1-wildfire.csv
  format: null
  id: resource_0a30b364
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: chad-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Colombia at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/79785092-85b0-44b6-a3bd-2ce31173d23e/download/colombia-admin1-wildfire.csv
  format: null
  id: resource_79785092
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: colombia-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for DR Congo at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/690ce34b-08f9-4fa4-8166-4e650ea3b4a1/download/dr-congo-admin1-wildfire.csv
  format: null
  id: resource_690ce34b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-congo-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Ethiopia at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/d105e72a-af1a-4052-85bc-d6ec39cabd5d/download/ethiopia-admin1-wildfire.csv
  format: null
  id: resource_d105e72a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Haiti at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/05be32bf-15ee-4322-a022-8bdfb135091e/download/haiti-admin1-wildfire.csv
  format: null
  id: resource_05be32bf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Mali at with admin1
    name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/35a4603a-0a34-4816-bede-7d4c4f923f13/download/mali-admin1-wildfire.csv
  format: null
  id: resource_35a4603a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mali-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Mozambique at
    with admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/bd453a85-671d-4dce-ad32-3cfed48798dc/download/mozambique-admin1-wildfire.csv
  format: null
  id: resource_bd453a85
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mozambique-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Myanmar at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/36996ce4-66ae-43a2-81e1-97e10dd7d388/download/myanmar-admin1-wildfire.csv
  format: null
  id: resource_36996ce4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: myanmar-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Niger at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/8b69053d-64f3-4bb4-b5f6-b4579d9f3d01/download/niger-admin1-wildfire.csv
  format: null
  id: resource_8b69053d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niger-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Nigeria at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/8b4bf058-60c8-48ff-92e6-3340766923d9/download/nigeria-admin1-wildfire.csv
  format: null
  id: resource_8b4bf058
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Somalia at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/1a4b7e00-c4b2-4c14-bc65-86d7af85149f/download/somalia-admin1-wildfire.csv
  format: null
  id: resource_1a4b7e00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for South Sudan at
    with admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/4b315308-8016-47c8-9e96-a4da95dbc7a3/download/south-sudan-admin1-wildfire.csv
  format: null
  id: resource_4b315308
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: south-sudan-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) wildfire extent for State of Palestine at with admin1
    name column
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/ac8cfbbe-e272-4465-9da6-a73000b36388/download/state-of-palestine-admin1-wildfire.csv
  format: null
  id: resource_ac8cfbbe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: state-of-palestine-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Sudan at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/a5e6996f-4c64-4fc8-9dcd-2dde61c1acbe/download/sudan-admin1-wildfire.csv
  format: null
  id: resource_a5e6996f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sudan-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) wildfire extent for Syrian Arab Republic at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/c4f8b993-7688-4bea-bcd0-8df618dadbc9/download/syrian-arab-republic-admin1-wildfire.csv
  format: null
  id: resource_c4f8b993
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syrian-arab-republic-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Ukraine at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/c4fde7a3-c79d-41bd-93e0-b9a137d8a6d5/download/ukraine-admin1-wildfire.csv
  format: null
  id: resource_c4fde7a3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Venezuela at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/a9d7c18d-85d6-404f-9a8f-925d3ebaafdd/download/venezuela-admin1-wildfire.csv
  format: null
  id: resource_a9d7c18d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: venezuela-admin1-wildfire.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for
    Disaster Risk Assessment (Gridded (4kmx4km) wildfire extent for Yemen at with
    admin1 name column)'
  download_url: https://data.humdata.org/dataset/ca740910-069b-4a78-92a8-595bd5b2c930/resource/1e709d31-6394-40f2-808a-cdc317235bee/download/yemen-admin1-wildfire.csv
  format: null
  id: resource_1e709d31
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yemen-admin1-wildfire.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ethzurich_wildfirehumanitarianrespo_2001
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
  - UGA
  - ZWE
  - ZMB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-01-01'
  start: '2001-01-01'
temporal_resolution: null
title: 'Wildfire: Humanitarian Response Plan (HRP) Countries Hazard Data for Disaster
  Risk Assessment'
version: null
vulnerability: null
---
