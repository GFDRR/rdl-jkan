---
attributions:
- entity:
    affiliation: null
    email: null
    name: ETH Zurich Climada
    url: https://data.humdata.org/dataset/climada-tropical-cyclone-dataset
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-tropical-cyclone-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-tropical-cyclone-dataset
dataset_id: rdls_hzd-ethzurich_tropicalcyclonehazarddata_1980
description: 'Tropical cyclone wind footprints (m/s) at 150 arcsec (approx 4 kilometers
  at equator) resolution. Available as global files and per country; available for
  historically observed records, and synthetically created, probabilistic events,
  from various modelling sources, for present and future climate scenarios.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/climada-tropical-cyclone-dataset]'
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
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Tropical cyclone wind hazard data generated from the Climada API using
    probabilistic modeling of historical cyclone records and synthetically created
    events. Wind speed footprints at 4 km resolution are provided for multiple countries,
    with data available for present climate conditions and future climate scenarios,
    aggregated to administrative level 1 boundaries.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/climada-tropical-cyclone-dataset
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
  url: https://doi.org/10.5194/nhess-21-393-2021
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://doi.org/10.5194/gmd-12-3085-2019
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://doi.org/10.5194/gmd-14-351-2021
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: tropical-cyclone wind speeds over the period 1980-202 at admin1 level
    for the HRP countries
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/d7ec31cc-becd-4e83-864d-705e60bc50a9/download/admin1-summaries-tropical-cyclone.csv
  format: null
  id: resource_d7ec31cc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: tropical-cyclone wind speeds by admin1 or admin2 for each flood for
    HRP countries
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/6416468e-bea9-4b50-8a8e-5bbdd4afa6dd/download/admin1-timeseries-summaries-tropical-cyclone.csv
  format: null
  id: resource_6416468e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-timeseries-summaries-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Colombia at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/3cd3aa9b-29ff-46c2-bb81-497acb930ab9/download/colombia-admin1-tropical-cyclone.csv
  format: null
  id: resource_3cd3aa9b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: colombia-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Ethiopia at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/2caae581-fefa-44fe-875d-19c0d39564a1/download/ethiopia-admin1-tropical-cyclone.csv
  format: null
  id: resource_2caae581
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Haiti at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/7f50b4f5-a621-452a-bf51-f3b321b030bb/download/haiti-admin1-tropical-cyclone.csv
  format: null
  id: resource_7f50b4f5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Mozambique at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/5327dbd0-b9d5-4058-b7f5-615582448a92/download/mozambique-admin1-tropical-cyclone.csv
  format: null
  id: resource_5327dbd0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mozambique-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Myanmar at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/3e8da305-b684-4cab-8817-f8e62d12fc3f/download/myanmar-admin1-tropical-cyclone.csv
  format: null
  id: resource_3e8da305
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: myanmar-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Somalia at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/4afd6798-c706-4141-b0dd-f8b777866242/download/somalia-admin1-tropical-cyclone.csv
  format: null
  id: resource_4afd6798
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Sudan at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/f346311a-2f06-4840-96ad-1c0b27e39267/download/sudan-admin1-tropical-cyclone.csv
  format: null
  id: resource_f346311a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sudan-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Venezuela at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/e28b1bda-3894-4c20-be48-1a5febda3adc/download/venezuela-admin1-tropical-cyclone.csv
  format: null
  id: resource_e28b1bda
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: venezuela-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Yemen at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/1b49a8a0-3bd5-4c89-ae72-e5cad362d4a6/download/yemen-admin1-tropical-cyclone.csv
  format: null
  id: resource_1b49a8a0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: yemen-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Afghanistan at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/d7f6aa17-1444-4030-9247-44e400ed9972/download/afghanistan-admin1-tropical-cyclone.csv
  format: null
  id: resource_d7f6aa17
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Burkina Faso at
    with admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/b05986dc-8efe-44ee-9c05-34bd0b2c4a33/download/burkina-faso-admin1-tropical-cyclone.csv
  format: null
  id: resource_b05986dc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burkina-faso-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Burundi at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/66ec4c20-6035-437c-b389-efb13bdbb010/download/burundi-admin1-tropical-cyclone.csv
  format: null
  id: resource_66ec4c20
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundi-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Cameroon at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/95c7a35d-1fcf-4c7f-93b8-3f67c7f63ed8/download/cameroon-admin1-tropical-cyclone.csv
  format: null
  id: resource_95c7a35d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cameroon-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Central African
    Republic at with admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/324ed0bd-cdb6-4b93-8651-d570a73a7a97/download/central-african-republic-admin1-tropical-cyclone.csv
  format: null
  id: resource_324ed0bd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: central-african-republic-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Chad at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/1e03a8ff-a238-4fd5-9140-8a305b7f0050/download/chad-admin1-tropical-cyclone.csv
  format: null
  id: resource_1e03a8ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: chad-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for DR Congo at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/37112b8f-de53-431c-86ab-d5dc89fc8a88/download/dr-congo-admin1-tropical-cyclone.csv
  format: null
  id: resource_37112b8f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-congo-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Mali at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/52cf4667-0ab4-4de4-8a13-85ff9bbcbc9c/download/mali-admin1-tropical-cyclone.csv
  format: null
  id: resource_52cf4667
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mali-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Niger at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/ad468699-1d7c-4b1c-9f5e-2f17caa8a05f/download/niger-admin1-tropical-cyclone.csv
  format: null
  id: resource_ad468699
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niger-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Nigeria at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/30c25e2f-73e1-4a43-b431-b0eb3948cca6/download/nigeria-admin1-tropical-cyclone.csv
  format: null
  id: resource_30c25e2f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nigeria-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Syrian Arab Republic
    at with admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/983f9af6-16a9-4ff7-ac8f-f7968526bfb5/download/syrian-arab-republic-admin1-tropical-cyclone.csv
  format: null
  id: resource_983f9af6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syrian-arab-republic-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Bangladesh at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/56c88397-8a61-463d-ae16-dcd7070bf336/download/bangladesh-admin1-tropical-cyclone.csv
  format: null
  id: resource_56c88397
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bangladesh-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Democratic People's
    Republic of Korea at with admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/27b71fa2-3692-4688-bcd4-5ff5a6326774/download/democratic-peoples-republic-of-korea-admin1-tropical-cyclone.csv
  format: null
  id: resource_27b71fa2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: democratic-people's-republic-of-korea-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Fiji at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/8cdd6fce-320f-47c3-b141-352564fda52b/download/fiji-admin1-tropical-cyclone.csv
  format: null
  id: resource_8cdd6fce
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fiji-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Indonesia at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/4f07c054-4647-4b42-8ce8-b94ba9e11ae8/download/indonesia-admin1-tropical-cyclone.csv
  format: null
  id: resource_4f07c054
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: indonesia-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Madagascar at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/bdce8e0a-df11-4afc-a4d1-d8893413a16b/download/madagascar-admin1-tropical-cyclone.csv
  format: null
  id: resource_bdce8e0a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: madagascar-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Nepal at with admin1
    name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/3a9e9148-f7f1-4944-bca3-dfe73a7252a4/download/nepal-admin1-tropical-cyclone.csv
  format: null
  id: resource_3a9e9148
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nepal-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Philippines at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/e7d04fd9-a130-4294-a293-e8529d6f9c91/download/philippines-admin1-tropical-cyclone.csv
  format: null
  id: resource_e7d04fd9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: philippines-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Sri Lanka at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/9d1a5e6d-8cb8-47c4-9881-385a57a49c06/download/sri-lanka-admin1-tropical-cyclone.csv
  format: null
  id: resource_9d1a5e6d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sri-lanka-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Vanuatu at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/c9b0b21a-ab9c-4ac2-a6d9-963521d28b76/download/vanuatu-admin1-tropical-cyclone.csv
  format: null
  id: resource_c9b0b21a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vanuatu-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Viet Nam at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/3744e260-29ce-4dac-a73f-352c5fc5d3d9/download/viet-nam-admin1-tropical-cyclone.csv
  format: null
  id: resource_3744e260
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: viet-nam-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Guatemala at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/84b51a40-84b5-4034-9e50-a47b53fd61bf/download/guatemala-admin1-tropical-cyclone.csv
  format: null
  id: resource_84b51a40
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guatemala-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for Honduras at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/76be1829-944e-42f1-baee-8512a1a1415a/download/honduras-admin1-tropical-cyclone.csv
  format: null
  id: resource_76be1829
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: honduras-admin1-tropical-cyclone.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) tropical-cyclone wind speeds for El Salvador at with
    admin1 name column
  download_url: https://data.humdata.org/dataset/f02bb601-9314-4162-9ebd-e1d18cdc2739/resource/9e2ded18-c4e6-4e31-994c-24cf0636dec5/download/el-salvador-admin1-tropical-cyclone.csv
  format: null
  id: resource_9e2ded18
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: el-salvador-admin1-tropical-cyclone.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ethzurich_tropicalcyclonehazarddata_1980
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  - VNM
  - YEM
  - COL
  - ETH
  - HTI
  - MOZ
  - MMR
  - SOM
  - SDN
  - AFG
  - BFA
  - BDI
  - CMR
  - CAF
  - TCD
  - COD
  - MLI
  - NER
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-25'
  start: '1980-01-02'
temporal_resolution: null
title: 'Tropical cyclone: Hazard Data for Disaster Risk Assessment (selected countries)'
version: null
vulnerability: null
---
