---
attributions:
- entity:
    affiliation: null
    email: null
    name: IBTrACS v02r01
    url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Japan Meteorological Agency (JMA)
    url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Joint Typhoon Warning Center (JTWC)
    url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Meteo France
    url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Australian Bureau of Meteorology
    url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
dataset_id: rdls_hzd-undrr_globalcyclonetracks_1969
description: 'This dataset includes a compilation of Tropical cyclones best tracks
  1969-2009.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cyclone-tracks-1969-2009]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries. The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Historical tropical cyclone best tracks compiled from IBTrACS v02r01
    (1969-2008) and supplemented with 2009 data from multiple meteorological agencies
    (JMA, JTWC, Meteo France, Australian Bureau of Meteorology). Track data were integrated
    into a GIS-based model to create a comprehensive global dataset of observed cyclone
    trajectories and characteristics.
  sources:
  - id: source_1
    license: null
    name: IBTrACS v02r01
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Japan Meteorological Agency (JMA)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Joint Typhoon Warning Center (JTWC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: Meteo France
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Australian Bureau of Meteorology
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cyclone-tracks-1969-2009
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
  url: http://www.ncdc.noaa.gov/oa/ibtracs/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global cyclone tracks (zipped shapefiles of cylone tracks (5,367 kb).)
  download_url: https://data.humdata.org/dataset/9309476b-6398-4f2c-96a8-4d73ac88f730/resource/18715546-6d8b-4a7c-a4cf-9c30b6e28742/download/cytracks.zip
  format: null
  id: resource_18715546
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cy_tracks.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_globalcyclonetracks_1969
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2009-01-01'
  start: '1969-01-01'
temporal_resolution: null
title: Global cyclone tracks
version: null
vulnerability: null
---
