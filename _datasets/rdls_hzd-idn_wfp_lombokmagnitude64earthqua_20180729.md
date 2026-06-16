---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite data
    url: https://data.humdata.org/dataset/lombok-indonesia-magnitude-6-4-earthquake-interferogram-using-sentinel-1-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/lombok-indonesia-magnitude-6-4-earthquake-interferogram-using-sentinel-1-data
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/lombok-indonesia-magnitude-6-4-earthquake-interferogram-using-sentinel-1-data
dataset_id: rdls_hzd-idn_wfp_lombokmagnitude64earthqua_20180729
description: 'An Interferogram of the devastating earthquake in Indonesia last July
  29, 2018 with a magnitude of 6.4. Data were processed using 2 Sentinel 1 data using
  repeat pass interferometry. One cycle (cold to hot color) means half of the radar
  wavelength which is approximately 3.5 - 7.5 cm wavelength. The data shows vertical
  ground displacement with respect to the satellites line of sight (LOS).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/lombok-indonesia-magnitude-6-4-earthquake-interferogram-using-sentinel-1-data]'
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
      intensity_measure: LOS:cm
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Two Sentinel-1 SAR acquisitions were processed using repeat-pass interferometry
    to generate an interferogram measuring vertical ground displacement (line-of-sight)
    from the 29 July 2018 Lombok earthquake. The interferometric phase was converted
    to displacement measurements with wavelength resolution of 3.5-7.5 cm per fringe
    cycle, providing post-event ground deformation observations.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite data
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lombok-indonesia-magnitude-6-4-earthquake-interferogram-using-sentinel-1-data
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
  description: Interferogram of the Magnitude 6.4 earthquake in Lombok, Indonesia
    (July 29, 2018)
  download_url: https://data.humdata.org/dataset/31bb8eca-f9fd-4c71-8744-e2a4033ca6fc/resource/6f133470-336e-4f58-873c-9995f6d8d226/download/indonesia.kmz
  format: null
  id: resource_6f133470
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Indonesia.kmz
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-idn_wfp_lombokmagnitude64earthqua_20180729
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-29'
temporal_resolution: null
title: Lombok Indonesia Magnitude 6.4 Earthquake Interferogram using Sentinel 1 data
version: null
vulnerability: null
---
