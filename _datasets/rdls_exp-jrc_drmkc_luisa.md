---
attributions:
- entity:
    affiliation: null
    email: jrc-risk-data-hub@ec.europa.eu
    name: European Commision (EC), Joint Research Centre (JRC)
    url: https://joint-research-centre.ec.europa.eu/
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: filipe.batista@ec.europa.eu
  name: Filipe Batista
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
creator:
  affiliation: null
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
- asset_type: null
  category: natural_environment
  id: exp_1
  metrics:
  - dimension: content
    id: luisa_2018
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type: null
    type: dataset
    url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: 'LUISA : Land-Use based Integrated Sustainability Assessment modelling platform'
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
publisher:
  affiliation: null
  email: jrc-ghsl-data@ec.europa.eu
  name: European Commission, Joint Research Centre
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
purpose: To provide high-resolution land use and land cover mapping across Europe
  with finer spatial and thematic detail for land accounting, modeling, and spatial
  planning applications.
referenced_by:
- author_names:
  - Filipe Batista
  - Cristian Pigaiani
  date_published: '2023-03-01'
  doi: https://doi.org/10.2760/503006
  id: Ref_1
  name: LUISA Base Map 2018
  url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
resources:
- access_url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Higher-detail LUISA basemap providing harmonized land-use/land-cover
    and cartographic context. Cell size: 50 m; suited for local to regional analyses
    and map production.'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/LUISA_basemap_020321_50m.tif
  format: null
  id: luisa_basemap_50m
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 50
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2018-01-01'
  temporal_resolution: null
  title: LUISA Basemap 50m spatial resolution
- access_url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Raster basemap from the LUISA framework showing harmonized land-use/land-cover
    and ancillary context for European territories. Cell size: 100 m; intended for
    visualization and overlay with hazard/exposure layers.'
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/LUISA_basemap_020321_100m.tif
  format: null
  id: luisa_basemap_100m
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 100
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2018-01-01'
  temporal_resolution: null
  title: LUISA Basemap 100m spatial resolution
- access_url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preconfigured ArcGIS (.lyr/.lyrx) symbology and render settings to
    display this dataset consistently (color ramps, classification, labels). Import
    into ArcGIS Pro/ArcMap to apply styles in one step.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/ARCGIS_legend_Base_Map_2018.lyr
  format: null
  id: arcgis_layerstyle
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2018-01-01'
  temporal_resolution: null
  title: ArcGIS Layer Style
- access_url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "QGIS (.qml) style file with predefined symbology, classification,\
    \ and labeling for consistent visualization. Load in QGIS via Layer Properties\
    \ \xE2\u2020\u2019 Style to apply immediately."
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/QGIS_legend_Base_Map_2018.qml
  format: null
  id: qgis_layerstyle
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2018-01-01'
  temporal_resolution: null
  title: QGIS Layer Style
- access_url: https://data.jrc.ec.europa.eu/dataset/51858b51-8f27-4006-bf82-53eba35a142c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Human-readable legend explaining classes, colors, and units used by
    the basemap/styles, including notes on classification rules and any special symbols
    in spreadsheet.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/LUISA/EUROPE/Basemaps/LandUse/2018/LATEST/Legend_Base_Map_2018.xlsx
  format: null
  id: legend
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2018-01-01'
  temporal_resolution: null
  title: Legend description
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_luisa
spatial:
  bbox: null
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: LUISA - Land Use-based Integrated Sustainability Assessment Base Map 2018
version: '1'
vulnerability: null
---
