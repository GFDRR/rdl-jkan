---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Space Agency Sentinel-1A C-band Synthetic Aperture Radar
    url: https://data.humdata.org/dataset/hawaii-mag6-9-earthquake-4may2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/hawaii-mag6-9-earthquake-4may2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/hawaii-mag6-9-earthquake-4may2018
dataset_id: rdls_hzd-usa_wfp_hawaiimay42018magnitude69_20180504
description: 'This is an interferogram of the Hawaii magnitude 6.9 earthquake followed
  by multiple volcanic eruptions of Kilauea volcano. Data source is Sentinel 1A C-band
  Synthetic Aperture Radar Interferometric Wide Swath provided by the European Space
  Agency. Best viewed in Google Earth Pro.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hawaii-mag6-9-earthquake-4may2018]'
details: This data should be interpreted with caution. Data shows vertical displacements
  with respect to radar Line of Sight (LOS) and does not equate to actual metric units.
  Data unit is in phase (radar wavelength per cycle). In case you need information
  on actual vertical displacement in meters, data needs a separate processing called
  phase unwrapping.
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sentinel-1A C-band SAR data acquired on May 2 and May 14, 2018 were
    processed using interferometric techniques to generate phase interferograms representing
    ground displacement from the May 4, 2018 magnitude 6.9 earthquake. The resulting
    interferogram is provided as a KML file for visualization in geospatial software.
  sources:
  - id: source_1
    license: null
    name: European Space Agency Sentinel-1A C-band Synthetic Aperture Radar
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hawaii-mag6-9-earthquake-4may2018
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is a Radar Interferogram of the 4 May 2018 Hawaii earthquake which
    is followed by volcanic activity in Kilauea volcano. Processed using Sentinel
    1A C-band SAR datasets.
  download_url: https://data.humdata.org/dataset/2583dd1d-1603-4583-ac2e-3c42587e3cdc/resource/ccb1bd67-0560-47b7-8aa7-49649903f3d0/download/phase_ifg_vv_02may2018_14may2018.kmz
  format: null
  id: resource_ccb1bd67
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Phase_ifg_VV_02May2018_14May2018.kmz
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-usa_wfp_hawaiimay42018magnitude69_20180504
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-04'
temporal_resolution: null
title: United States - Hawaii May 4, 2018 magnitude 6.9 earthquake Interferogram using
  Sentinel 1A C-band SAR
version: null
vulnerability: null
---
