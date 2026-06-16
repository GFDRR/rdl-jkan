---
attributions:
- entity:
    affiliation: null
    email: null
    name: ANSS Comprehensive Catalog (ComCat)
    url: https://data.humdata.org/dataset/catalog-of-earthquakes1970-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/catalog-of-earthquakes1970-2014
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/catalog-of-earthquakes1970-2014
dataset_id: rdls_hzd-undrr_globalcatalogearthquakes_1970
description: 'Catalog of Earthquakes 1970-2014, Source: ANSS - USGS The ANSS Comprehensive
  Catalog (ComCat) contains earthquake source parameters (e.g. hypocenters, magnitudes,
  phase picks and amplitudes) and other products (e.g. moment tensor solutions, macroseismic
  information, tectonic summaries, maps) produced by contributing seismic networks..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/catalog-of-earthquakes1970-2014]'
details: 'This dataset was generated using other global datasets; it should not be
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
  or concerning the delimitation of its frontiers or boundaries. Disclaimer: The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.'
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Earthquake source parameters were compiled from the ANSS Comprehensive
    Catalog (ComCat), a multi-network observational dataset maintained by USGS. The
    catalog contains direct observational data from seismic networks including hypocenters,
    magnitudes, phase picks, amplitudes, and derived products such as moment tensor
    solutions and macroseismic information for the period 1970-2014.
  sources:
  - id: source_1
    license: null
    name: ANSS Comprehensive Catalog (ComCat)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/catalog-of-earthquakes1970-2014
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global catalog of earthquakes (Zipped shapefiles of earthquakes catalogue
    from 1970-2014 (264kb))
  download_url: https://data.humdata.org/dataset/4881d82b-ba63-4515-b748-c364f3d05b42/resource/5d4ed071-d580-40d9-95a5-5a001fc02f30/download/earthquakes1970-2014.zip
  format: null
  id: resource_5d4ed071
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: earthquakes1970-2014.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global catalog of earthquakes (Json file of earthquakes catalogue from
    1970-2014 (1,552 kb))
  download_url: https://data.humdata.org/dataset/4881d82b-ba63-4515-b748-c364f3d05b42/resource/e5722a70-d599-47b9-b7b8-17ed63107076/download/earthquakes1970-2014.json
  format: null
  id: resource_e5722a70
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: earthquakes1970-2014.json
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global catalog of earthquakes (Csv file of earthquakes catalogue from
    1970 to 2014 (602 kb).)
  download_url: https://data.humdata.org/dataset/4881d82b-ba63-4515-b748-c364f3d05b42/resource/10ac8776-5141-494b-b3cd-bf7764b2f964/download/earthquakes1970-2014.csv
  format: null
  id: resource_10ac8776
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: earthquakes1970-2014.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_globalcatalogearthquakes_1970
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
  end: '2014-12-31'
  start: '1970-01-01'
temporal_resolution: null
title: Global catalog of earthquakes
version: null
vulnerability: null
---
