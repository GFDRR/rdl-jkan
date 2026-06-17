---
attributions:
- entity:
    affiliation: null
    email: null
    name: ESA Sentinel-1
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: JAXA ALOS PALSAR 2
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: TerraSAR-X
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Landsat
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WASDI Fadeout
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-ASIA Asian Institute of Technology
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_7
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: DLR German Aerospace Agency
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_8
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Earth Observatory of Singapore
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_9
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NASA Disaster
    url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
  id: attribution_10
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
dataset_id: rdls_hzd-bgdind_wfp_cycloneamphanflooddetecte_202006
description: 'This data combines satellite detected water (flooding) for Bangladesh
  and north-east India during cyclone AMPHAN. This flood raster includes data from
  ESA Sentinel-1, JAXA ALOS PALSAR 2, TerraSAR-X, MODIS, Landsat and Sentinel 1. The
  organisations involved in the processing of the data are WASDI Fadeout, Sentinel-ASIA
  Asian Institute of Technology, DLR German Aerospace Agency, Earth Observatory of
  Singapore (EOS), NASA Disaster and Bob Adler from University of Colorado.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india]'
details: null
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
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Satellite-detected flood water extent derived from multi-sensor synthetic
    aperture radar (Sentinel-1, ALOS PALSAR 2, TerraSAR-X) and optical imagery (MODIS,
    Landsat) acquired during cyclone Amphan. Data were processed by multiple international
    agencies and platforms (WASDI, Sentinel-ASIA, DLR, EOS, NASA) to generate a composite
    flood raster map showing inundated areas in Bangladesh and north-east India.
  sources:
  - id: source_1
    license: null
    name: ESA Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: JAXA ALOS PALSAR 2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: TerraSAR-X
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Landsat
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: WASDI Fadeout
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_7
    license: null
    name: Sentinel-ASIA Asian Institute of Technology
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_8
    license: null
    name: DLR German Aerospace Agency
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_9
    license: null
    name: Earth Observatory of Singapore
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_10
    license: null
    name: NASA Disaster
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cyclone-amphan-flood-detected-water-for-bangladesh-and-india
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
  description: Cyclone Amphan flood detected water for Bangladesh and India (20-31
    May, 2020)
  download_url: https://data.humdata.org/dataset/4b05abad-410b-4323-b906-e8808146b5d5/resource/407e70ce-5a5f-40a5-b418-967e846f5e06/download/amphan_flood_total_all.tif
  format: null
  id: resource_407e70ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: amphan_flood_total_all.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgdind_wfp_cycloneamphanflooddetecte_202006
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  - IND
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-06-30'
  start: '2020-06-20'
temporal_resolution: null
title: Cyclone Amphan flood detected water for Bangladesh and India
version: null
vulnerability: null
---
