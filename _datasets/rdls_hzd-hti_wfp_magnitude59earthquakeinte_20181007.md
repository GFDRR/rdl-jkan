---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 Copernicus
    url: https://data.humdata.org/dataset/haiti-magnitude-5-0-earthquake-interferogram
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/haiti-magnitude-5-0-earthquake-interferogram
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/haiti-magnitude-5-0-earthquake-interferogram
dataset_id: rdls_hzd-hti_wfp_magnitude59earthquakeinte_20181007
description: 'Sentinel 1 interferogram of Haiti Magnitude 5.9 earthquake on Oct 7,
  2018. Images used were 26 September and 8 October 2018.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/haiti-magnitude-5-0-earthquake-interferogram]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-4.0
lineage:
  description: Sentinel-1 SAR images acquired on 26 September and 8 October 2018 were
    processed using interferometric techniques to generate a phase interferogram (VV
    polarization) that captures ground surface deformation caused by the magnitude
    5.9 earthquake on 7 October 2018 in Haiti.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-magnitude-5-0-earthquake-interferogram
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
  description: Haiti magnitude 5.9 earthquake (south of epicenter)
  download_url: https://data.humdata.org/dataset/212d4e38-7e0c-4a4f-af2a-d851d593aaf3/resource/97f75e6c-5d38-4707-b95b-557241b61143/download/phase_ifg_vv_08oct2018_26sep2018.kmz
  format: null
  id: resource_97f75e6c
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Phase_ifg_VV_08Oct2018_26Sep2018.kmz
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_wfp_magnitude59earthquakeinte_20181007
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-10-07'
temporal_resolution: null
title: Haiti Magnitude 5.9 Earthquake Interferogram
version: null
vulnerability: null
---
