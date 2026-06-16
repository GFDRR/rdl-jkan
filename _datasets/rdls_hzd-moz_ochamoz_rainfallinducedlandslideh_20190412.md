---
attributions:
- entity:
    affiliation: null
    email: null
    name: Mozambique National Disasters Management Institute
    url: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ADRF Sub Saharan Africa Risk Profiles project
    url: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index
dataset_id: rdls_hzd-moz_ochamoz_rainfallinducedlandslideh_20190412
description: 'Layer provides distribution of landslide hazard, describing by an index
  of very low to very high hazard. Data produced under the ADRF Sub Saharan Africa
  Risk Profiles project. The project provides also risk data produced, exposure and
  hazard data used in the analyses.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index]'
details: null
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
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Landslide hazard index derived from direct observational and anecdotal
    data collected by Mozambique National Disasters Management Institute, processed
    and classified into a susceptibility index ranging from very low to very high
    under the ADRF Sub Saharan Africa Risk Profiles project to characterize rainfall-induced
    landslide hazard distribution.
  sources:
  - id: source_1
    license: null
    name: Mozambique National Disasters Management Institute
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: ADRF Sub Saharan Africa Risk Profiles project
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-rainfall-induced-landslide-hazard-index
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
  description: Shapefile of distribution of landslide hazard, describing by an index
    of very low to very high hazard
  download_url: http://geonode.ingc.gov.mz/qgis-server/download-zip/moz_haz_rn_2010?access_token=27cdcae85d3711e9932e02967b3ca6c8
  format: null
  id: resource_79d3bae2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_haz_rn_2010.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Distribution of landslide hazard, describing by an index of very low
    to very high hazard in GeoTIFF format.
  download_url: http://geonode.ingc.gov.mz/qgis-server/geotiff/moz_haz_rn_2010?access_token=27cdcae85d3711e9932e02967b3ca6c8
  format: null
  id: resource_58635362
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: moz_haz_rn_2010.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_ochamoz_rainfallinducedlandslideh_20190412
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-04-12'
temporal_resolution: null
title: Mozambique Rainfall-Induced Landslide Hazard Index
version: null
vulnerability: null
---
