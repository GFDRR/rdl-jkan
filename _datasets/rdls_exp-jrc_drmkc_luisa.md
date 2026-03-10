---
catalog: null
contact_point:
  email: filipe.batista@ec.europa.eu
  name: Filipe Batista
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
creator:
  email: jrc-ghsl-data@ec.europa.eu
  name: European Commission, Joint Research Centre
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
dataset_id: rdls_exp-jrc_drmkc_luisa
description: High-resolution land use/land cover map from LUISA modelling platform
details: LUISA Base Map delivers higher spatial detail and finer thematic breakdown
  of land use/cover categories (17 categories) compared to CORINE (11 categories),
  covering EU27 and additional European countries including Albania, Bosnia and Herzegovina,
  Iceland, Kosovo, Liechtenstein, Montenegro, North Macedonia, Norway, Serbia, Switzerland,
  Turkey, and United Kingdom. The map has a minimum mapping unit (MMU) of 1 hectare
  for artificial surfaces and 5 hectares for non-artificial surfaces, with pixel resolution
  of 50-100m. The 2018 edition refines CORINE Land Cover 2018 through automated geospatial
  data fusion, integrating information from Copernicus High Resolution Layers, Urban
  Atlas, Global Human Settlement Layer, CLC Change Maps, and other trusted datasets.
  This uniform methodology using European-wide remotely sensed imagery ensures high
  comparability across countries, making it suitable for applications requiring fine
  spatial and thematic detail of land use/cover consistently across Europe.
exposure:
  category: natural_environment
  dimension: content
  quantity_kind: area
  taxonomy: null
hazard: null
license: CC-BY-4.0
loss: null
project: 'LUISA : Land-Use based Integrated Sustainability Assessment modelling platform'
publisher:
  email: jrc-ghsl-data@ec.europa.eu
  name: European Commission, Joint Research Centre
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
purpose: To provide high-resolution land use and land cover mapping across Europe
  with finer spatial and thematic detail for land accounting, modeling, and spatial
  planning applications.
resources:
- coordinate_system: EPSG:4326
  description: 'Higher-detail LUISA basemap providing harmonized land-use/land-cover
    and cartographic context. Cell size: 50 m; suited for local to regional analyses
    and map production.'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/LUISA_basemap_020321_50m.tif
  format: geotiff
  id: luisa_basemap_50m
  spatial_resolution: 50
  title: LUISA Basemap 50m spatial resolution
- coordinate_system: EPSG:4326
  description: 'Raster basemap from the LUISA framework showing harmonized land-use/land-cover
    and ancillary context for European territories. Cell size: 100 m; intended for
    visualization and overlay with hazard/exposure layers.'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/LUISA_basemap_020321_100m.tif
  format: geotiff
  id: luisa_basemap_100m
  spatial_resolution: 100
  title: LUISA Basemap 100m spatial resolution
- coordinate_system: null
  description: Preconfigured ArcGIS (.lyr/.lyrx) symbology and render settings to
    display this dataset consistently (color ramps, classification, labels). Import
    into ArcGIS Pro/ArcMap to apply styles in one step.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/ARCGIS_legend_Base_Map_2018.lyr
  format: website
  id: arcgis_layerstyle
  spatial_resolution: null
  title: ArcGIS Layer Style
- coordinate_system: null
  description: "QGIS (.qml) style file with predefined symbology, classification,\
    \ and labeling for consistent visualization. Load in QGIS via Layer Properties\
    \ \xE2\u2020\u2019 Style to apply immediately."
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/QGIS_legend_Base_Map_2018.qml
  format: website
  id: qgis_layerstyle
  spatial_resolution: null
  title: QGIS Layer Style
- coordinate_system: null
  description: Human-readable legend explaining classes, colors, and units used by
    the basemap/styles, including notes on classification rules and any special symbols
    in spreadsheet.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/Legend_Base_Map_2018.xlsx
  format: website
  id: legend
  spatial_resolution: null
  title: Legend description
risk_data_type:
- exposure
schema: rdl-02
slug: rdls_exp-jrc_drmkc_luisa
spatial:
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
title: LUISA - Land Use-based Integrated Sustainability Assessment Base Map 2018
version: '1'
vulnerability: null
---
