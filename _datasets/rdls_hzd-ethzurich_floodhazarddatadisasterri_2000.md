---
attributions:
- entity:
    affiliation: null
    email: null
    name: Cloud to Street Database
    url: https://data.humdata.org/dataset/climada-flood-dataset
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ETH Zurich Climada
    url: https://data.humdata.org/dataset/climada-flood-dataset
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-flood-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-flood-dataset
dataset_id: rdls_hzd-ethzurich_floodhazarddatadisasterri_2000
description: 'Flood footprint of historical events at a 200m x 200m resolution based
  on the cloud to street database with events from years 2000-2018 (see https://floodbase.com).
  The events have been processed into one hazard dataset per country.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/climada-flood-dataset]'
details: In this API we provide datasets in a form that can readily be used in CLIMADA
  analyses. Users should determine whether these datasets are suitable for a particular
  purpose or application, considering factors such as resolution (for example, a 4km
  grid is not suitable for modelling risk at the neighborhood level), the way that
  hazards are represented in the dataset (for example, specific events, event thresholds,
  probabilistic event sets, etc.), the way that exposure is represented, and other
  aspects. Data provided with no warranty of any kind under CC BY 4.0. See respective
  [API metadata](https://climada.ethz.ch/data-types/) for details and limitations.
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Historical flood events from 2000-2018 were extracted from the Cloud
    to Street satellite-derived flood database and processed through the Climada API
    to generate country-level flood footprint datasets at 200m resolution. The resulting
    hazard data represents observed flood extents aggregated by administrative boundaries.
  sources:
  - id: source_1
    license: null
    name: Cloud to Street Database
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
- href: https://data.humdata.org/dataset/climada-flood-dataset
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
  url: https://climada-python.readthedocs.io/en/stable/tutorial/climada_util_api_client.html
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Congo at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/3cabe801-3563-4765-9476-3f3f1c151318/download/congo-admin1-flood.csv
  format: null
  id: resource_3cabe801
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: congo-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Flood: Hazard Data for Disaster Risk Assessment (selected countries)
    (Flood extent over the period 2002-2018 at admin1 level for the HRP countries)'
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/48eeeeff-9b12-4cb8-8351-f6f18f9cbd23/download/admin1-summaries-flood.csv
  format: null
  id: resource_48eeeeff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Flood: Hazard Data for Disaster Risk Assessment (selected countries)
    (Flood extent by admin1 or admin2 for each flood for HRP countries)'
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/5b49391f-4251-4e5b-977a-ee1ea49e2034/download/admin1-timeseries-summaries-flood.csv
  format: null
  id: resource_5b49391f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-timeseries-summaries-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Afghanistan at with admin1 name
    column - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/346fc6c6-5e8e-4eb0-86ef-070003529ed8/download/afghanistan-admin1-flood.csv
  format: null
  id: resource_346fc6c6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Burundi at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/fabff473-3af6-404e-9823-8275588cbfdb/download/burundi-admin1-flood.csv
  format: null
  id: resource_fabff473
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundi-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Central African Republic at with
    admin1 name column - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/d15f98ca-cb1f-4955-98b7-8b3625b991a4/download/central-african-republic-admin1-flood.csv
  format: null
  id: resource_d15f98ca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: central-african-republic-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Chad at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/07b56edd-9a9b-4d41-a5d4-86281781aebd/download/chad-admin1-flood.csv
  format: null
  id: resource_07b56edd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: chad-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Colombia at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/53a301ef-b574-4ab2-8ea6-785db4f537f8/download/colombia-admin1-flood.csv
  format: null
  id: resource_53a301ef
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: colombia-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for DR Congo at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/82acda41-398f-48f9-ac84-2e812fb2871c/download/dr-congo-admin1-flood.csv
  format: null
  id: resource_82acda41
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-congo-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Ethiopia at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/2f2d287f-d92d-4808-8bb6-ac3692abc5a2/download/ethiopia-admin1-flood.csv
  format: null
  id: resource_2f2d287f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Haiti at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/b9c7bca5-c97a-459f-bfd5-9cf0614971fc/download/haiti-admin1-flood.csv
  format: null
  id: resource_b9c7bca5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Mali at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/15a0aaf4-adc3-4696-817f-cbe4c586b3ea/download/mali-admin1-flood.csv
  format: null
  id: resource_15a0aaf4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mali-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Mozambique at with admin1 name
    column - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/9961ec54-e476-499d-a801-40577ee7276f/download/mozambique-admin1-flood.csv
  format: null
  id: resource_9961ec54
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mozambique-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Myanmar at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/796986b9-038f-416c-ad9c-9c0317d72b91/download/myanmar-admin1-flood.csv
  format: null
  id: resource_796986b9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: myanmar-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Niger at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/11ce8449-0dd4-4d6e-9156-32ab430a410c/download/niger-admin1-flood.csv
  format: null
  id: resource_11ce8449
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niger-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Nigeria at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/c17b749d-bc30-47b2-9cdf-77b17e6a94e4/download/nigeria-admin1-flood.csv
  format: null
  id: resource_c17b749d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Somalia at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/97e6bd36-4150-4e49-b5a8-04c3b2c1d97e/download/somalia-admin1-flood.csv
  format: null
  id: resource_97e6bd36
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Sudan at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/92cbe180-7db3-42ef-aad1-72596d65f5c5/download/sudan-admin1-flood.csv
  format: null
  id: resource_92cbe180
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sudan-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Syrian Arab Republic at with admin1
    name column - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/c17544c9-83ce-4e48-8d49-d19620e71c28/download/syrian-arab-republic-admin1-flood.csv
  format: null
  id: resource_c17544c9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syrian-arab-republic-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Ukraine at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/7bd19bae-e253-484c-856f-a6bbf6c3a459/download/ukraine-admin1-flood.csv
  format: null
  id: resource_7bd19bae
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Venezuela at with admin1 name
    column - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/8d689a02-7349-4965-b1b2-2bbd46d3c826/download/venezuela-admin1-flood.csv
  format: null
  id: resource_8d689a02
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: venezuela-admin1-flood.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (200mx200m) flood extent for Yemen at with admin1 name column
    - non flood grid points ommitted
  download_url: https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/83956a5a-10b4-4570-adb1-9d35f1e37563/download/yemen-admin1-flood.csv
  format: null
  id: resource_83956a5a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yemen-admin1-flood.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ethzurich_floodhazarddatadisasterri_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - SYR
  - VEN
  - YEM
  - COG
  - AFG
  - BDI
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
  - SDN
  - UKR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-07-15'
  start: '2000-04-05'
temporal_resolution: null
title: 'Flood: Hazard Data for Disaster Risk Assessment (selected countries)'
version: null
vulnerability: null
---
