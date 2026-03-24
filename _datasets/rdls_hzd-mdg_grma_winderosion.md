---
catalog: null
contact_point:
  email: science@axaclimate.com
  id: attribution_contact_point_001
  name: AXA Climate
  url: null
creator:
  email: null
  id: attribution_creator_001
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_winderosion
description: Wind erodible fraction analysis examining soil texture and chemical properties
  to identify dust storm emission sources across Madagascar.
details: The wind erodible fraction examines the top 0-5 cm layer of soil's texture
  and chemical properties, indicates the soil susceptibility to erosion. The soil
  erodible fraction is determined based on the methodology developed by Fryrear et
  al. (1994) and data extracted from the SoilGrids database (Hengl et al., 2017).
  The wind erodible fraction is overlayed with the bare soil and shrubland locations
  to highlight potential dust storm emission sources.
exposure: []
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: strong_wind
  intensity: MHI:-
  occurrence_range: ''
  processes: extratropical_cyclone
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  email: null
  id: attribution_publisher_001
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
resources:
- coordinate_system: EPSG:4326
  description: SoilGrids is a system for global digital soil mapping that uses state-of-the-art
    machine learning methods to map the spatial distribution of soil properties across
    the globe.
  download_url: https://soilgrids.org/
  format: GeoTIFF (tif)
  id: resource_szweUR0z
  media_type: null
  spatial_resolution: 1000
  temporal: null
  title: SoilGrids database
- coordinate_system: EPSG:4326
  description: High resolution land cover from ESA's WorldCover data v200. The bare/sparse
    vegetation and shrubland grid points are extracted to describe regions that can
    become dust emission sources.
  download_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  format: GeoTIFF (tif)
  id: resource_XRXrhsbL
  media_type: null
  spatial_resolution: 10
  temporal:
    duration: null
    end: '2021'
    start: '2021'
    temporal_resolution: null
  title: Bare soil and shrubland
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-mdg_grma_winderosion
spatial:
  countries:
  - MDG
  scale: national
title: Wind erosion
version: '1.0'
vulnerability: null
---
