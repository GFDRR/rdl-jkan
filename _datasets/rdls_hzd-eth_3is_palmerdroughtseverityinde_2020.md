---
attributions:
- entity:
    affiliation: null
    email: null
    name: Google Earth Engine
    url: https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: TerraClimate
    url: https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024
dataset_id: rdls_hzd-eth_3is_palmerdroughtseverityinde_2020
description: "This dataset provides Palmer Drought Severity Index (PDSI) values for\
  \ Ethiopia from 2020 to 2024, offering insights into drought conditions across the\
  \ country. The PDSI is a widely used drought index that measures deviations in soil\
  \ moisture conditions from the long-term average, helping to identify both drought\
  \ and wet conditions. Unlike traditional PDSI calculations that rely on the Thornthwaite\
  \ method for estimating potential evapotranspiration (ET), this dataset utilizes\
  \ a more physically based Penman-Monteith reference ET, which accounts for: Solar\
  \ radiation Temperature Humidity Windspeed Interpretation of PDSI Values: PDSI between\
  \ -0.5 and 0.5 \u2192 Near-normal soil moisture conditions PDSI < -4 \u2192 Extreme\
  \ drought PDSI > 4 \u2192 Very wet conditions. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PDSI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: PDSI values were computed from remote sensing data accessed via Google
    Earth Engine, utilizing TerraClimate climate inputs and a physically-based Penman-Monteith
    method for potential evapotranspiration estimation rather than the traditional
    Thornthwaite approach. The resulting drought index measures deviations in soil
    moisture conditions from long-term averages across Ethiopia for the 2020-2024
    period.
  sources:
  - id: source_1
    license: null
    name: Google Earth Engine
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: TerraClimate
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-palmer-drought-severity-index-pdsi-2020-2024
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
  description: Ethiopia - Palmer Drought Severity Index (PDSI) - 2022-2024.png
  download_url: https://data.humdata.org/dataset/ee3b87ce-ff6d-433b-89db-faa25337954e/resource/23dfe928-f9bb-482d-9e62-50480e16fb3a/download/ethiopia-palmer-drought-severity-index-pdsi-2022-2024.png
  format: PNG
  id: resource_23dfe928
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia - Palmer Drought Severity Index (PDSI) - 2022-2024.png
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Palmer Drought Severity Index (PDSI) (PSDI TerraClimate
    - 2020-2024.pdf)
  download_url: https://data.humdata.org/dataset/ee3b87ce-ff6d-433b-89db-faa25337954e/resource/e6eb79ba-f940-49ec-9757-58c07d1ce3bf/download/psdi-terraclimate-2020-2024.pdf
  format: null
  id: resource_e6eb79ba
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PSDI TerraClimate - 2020-2024.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Palmer Drought Severity Index (PDSI) (PSDI TerraClimate
    - 2020-2024.xlsx)
  download_url: https://data.humdata.org/dataset/ee3b87ce-ff6d-433b-89db-faa25337954e/resource/10609243-8e62-408f-a553-198c4f3a0ff8/download/psdi-terraclimate-2020-2024.xlsx
  format: null
  id: resource_10609243
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PSDI TerraClimate - 2020-2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Palmer Drought Severity Index (PDSI) (Administrative Boundaries
    Level 1 - Region)
  download_url: https://data.humdata.org/dataset/ee3b87ce-ff6d-433b-89db-faa25337954e/resource/ae275c78-427a-4f38-8dc8-9c4d867f0971/download/admin1.kml
  format: null
  id: resource_ae275c78
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Admin1.kml
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_3is_palmerdroughtseverityinde_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Ethiopia - Palmer Drought Severity Index (PDSI)
version: null
vulnerability: null
---
