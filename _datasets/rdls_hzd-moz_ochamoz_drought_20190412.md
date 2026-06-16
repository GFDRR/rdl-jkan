---
attributions:
- entity:
    affiliation: null
    email: null
    name: Mozambique National Disasters Management Institute
    url: https://data.humdata.org/dataset/mozambique-drought
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ADRF Sub Saharan Africa Risk Profiles project
    url: https://data.humdata.org/dataset/mozambique-drought
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-drought
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-drought
dataset_id: rdls_hzd-moz_ochamoz_drought_20190412
description: 'Data produced under the ADRF Sub Saharan Africa Risk Profiles project.
  The project provides also risk data produced, exposure and hazard data used in the
  analyses.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-drought]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Drought hazard data generated using a soil water balance approach applied
    to global geospatial raster datasets (precipitation, evapotranspiration, rooted
    soil depth, water holding capacity) analyzed on a seasonal basis to quantify accumulated
    transpiration and derive Standardized Precipitation Index values across Mozambique
    at 30-arcsecond resolution.
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
- href: https://data.humdata.org/dataset/mozambique-drought
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
  description: Mozambique Drought (Drought indicators in raster format for Mozambique)
  download_url: http://geonode.ingc.gov.mz/qgis-server/geotiff/euwatch_spi_mozambique_r25_30s_clipped?access_token=bb3efa145d1311e9932e02967b3ca6c8
  format: null
  id: resource_3d5df070
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: euwatch_spi_mozambique_r25_30s_clipped.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_ochamoz_drought_20190412
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
title: Mozambique Drought
version: null
vulnerability: null
---
