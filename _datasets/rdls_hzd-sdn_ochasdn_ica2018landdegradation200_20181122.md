---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA MODIS 2001-2012
    url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldClim 1970-2000
    url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FAO and NASA SRTM Digital Elevation Model
    url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HQ OSEP GIS Analysis
    url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
dataset_id: rdls_hzd-sdn_ochasdn_ica2018landdegradation200_20181122
description: 'This layer contains information about the land degradation phenomenon
  - by second-level administrative area - observed for the purposes of the Integrated
  Context Analysis (ICA) run in Sudan in 2018. Data sources: HQ OSEP GIS Analysis
  of NASA MODIS 2001-2012, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
  Model data. The main indicators used for the analysis were the average ecological
  changes observed between 2001-2005 and 2009-2013 and the percentage of erosion-prone
  surface.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013]'
details: https://geonode.wfp.org/layers/geonode%3Asdn_ica_landdegradation_geonode_20180201
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: Er:T/ha
      process: soil_erosion
      trigger: null
      type: erosion
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Multi-source satellite and topographic data (MODIS 2001-2012, WorldClim,
    SRTM DEM) were integrated through HQ OSEP GIS analysis to quantify ecological
    changes between two 5-year periods (2001-2005 vs 2009-2013) and identify erosion-prone
    surfaces. Results were aggregated and classified at second-level administrative
    boundaries to produce a land degradation hazard assessment for the 2018 Sudan
    Integrated Context Analysis.
  sources:
  - id: source_1
    license: null
    name: NASA MODIS 2001-2012
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldClim 1970-2000
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: FAO and NASA SRTM Digital Elevation Model
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: HQ OSEP GIS Analysis
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ica-sudan-2018-land-degradation-2001-2013
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: https://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Asdn_ica_landdegradation_geonode_20180201&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    - by second-level administrative area - observed for the purposes of the Integrated
    Context Analysis (ICA) run in Sudan in 2018. Data sources: HQ OSEP GIS Analysis
    of NASA MODIS 2001-2012, WorldClim 1970-2000, FAO and NASA SRTM Digital Elevation
    Model data. The main indicators used for the analysis were the average ecological
    changes observed between 2001-2005 and 2009-2013 and the percentage of erosion-prone
    surface.'
  download_url: null
  format: null
  id: resource_3ec6a277
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Sudan, 2018 - Land Degradation, 2001-2013
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_ochasdn_ica2018landdegradation200_20181122
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-22'
temporal_resolution: null
title: ICA Sudan, 2018 - Land Degradation, 2001-2013
version: null
vulnerability: null
---
