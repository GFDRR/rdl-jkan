---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACORAB
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: BAN
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Infoasaid
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Audio Visual Electronic
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sushmit International
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Field assessment
    url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internews (inactive)
  url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
creator:
  affiliation: null
  email: null
  name: Internews (inactive)
  url: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
dataset_id: rdls_exp-npl_internews_radiostationsstatusareasa_20150515
description: 'This assessment of the radio stations in the areas affected by the Nepal
  earthquake includes information on station name, location, operating status, damage,
  and contact information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas]'
details: If coordinates have not been gathered the address information has been cross
  referenced with the Nepal government VDC (admin-4) p-codes. Operating status information
  was collected in the time period between the April 25 and May 12 earthquakes and
  may not account for changes from May 12 onward.
exposure:
- asset_type:
    description: Radio station facilities and their operational status in earthquake-affected
      areas
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
  description: Radio station infrastructure inventory compiled from 7 sources including
    contact registries (ACORAB, BAN) and geographic databases (Infoasaid, Audio Visual
    Electronic, Sushmit International) supplemented by field assessment. Station locations
    were geocoded and operational status documented in the 2015 Nepal earthquake-affected
    areas.
  sources:
  - id: source_1
    license: null
    name: ACORAB
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: BAN
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Infoasaid
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: Audio Visual Electronic
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_5
    license: null
    name: Sushmit International
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_6
    license: null
    name: Field assessment
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/radio-stations-in-earthquake-affected-areas
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
  description: This data contains name, location and operating status of radio stations
    in areas affected by the 2015 Nepal earthquake
  download_url: https://data.humdata.org/dataset/50fce656-9dcd-41df-8ba9-ee2367651b29/resource/0ba19f55-907d-4c89-8c3c-179d335da32f/download/radio-station-assessment-of-nepal-earthquake-affected-areas.csv
  format: null
  id: resource_0ba19f55
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Radio Station Assessment of Nepal Earthquake Affected Areas.CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This data set is a compilation of stations organized by VDC (admin-4).
    This enables all stations to be visualized even those without latitude and longitude
    coordinates.
  download_url: https://data.humdata.org/dataset/50fce656-9dcd-41df-8ba9-ee2367651b29/resource/0d620974-ac2d-4ab7-813c-b5d0a3eddf3d/download/radio-station-in-affected-districts-all-stations-count.xlsx
  format: null
  id: resource_0d620974
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Districts Counts of Radio Stations in Earthquake Affected Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is a shapefile containing merged counts of radio stations with
    Nepal's VDC boundaries layer.
  download_url: https://data.humdata.org/dataset/50fce656-9dcd-41df-8ba9-ee2367651b29/resource/26baec9a-c1cd-4031-b482-218cefc19614/download/vdc-counts-of-radio-stations-in-affected-areas.zip
  format: null
  id: resource_26baec9a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VDC_counts_of_radio_stations_in_affected_areas.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_internews_radiostationsstatusareasa_20150515
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-05-15'
temporal_resolution: null
title: Radio Stations Status in Areas Affected by 2015 Nepal Earthquake
version: null
vulnerability: null
---
