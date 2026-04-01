---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: info@haskoning.com
  id: attribution_creator
  name: Royal HaskoningDHV
  url: https://www.haskoning.com/
dataset_id: rdls_hevl-gmb_iucrp_floodcoastres
description: Risk data package for the Greater Banjul Area (GBA), The Gambia, providing
  flood hazard (urban/pluvial maximum water depth and coastal flat water-level scenarios),
  coastal erosion hazard zones, exposure layers (land use, critical facilities, essential
  access routes, study boundaries), and derived risk/loss rasters for baseline and
  future horizons (2020, 2040, 2070).
details: 'Inventory review indicates the package includes: (i) flood hazard GeoTIFFs
  under `02 Flood hazard` for Urban (21 rasters; return period labels T04, T1, T5,
  T10, T25, T100, T250 across horizons current/2040/2070) and Coastal (15 rasters;
  flat scenario water level in meters across 2020/2040/2070 with labels 0.4/1/10/30/100);
  (ii) coastal erosion vectors in `Erosion hazard.gdb` (2040/2070 erosion zones plus
  Jan 2020 reference coastline); (iii) exposure vectors in `Landuse.gdb` (land use
  polygons, critical facilities points/polygons, essential roads) and `Areas.gdb`
  (areas and project boundary); and (iv) downstream outputs in `04 Risk` (9 risk rasters
  for Coastal/Urban/Combined x 2020/2040/2070) and `05 Damage` (33 GeoTIFF rasters,
  with naming patterns indicating max water depth and flat scenario layers; unit/meaning
  should be confirmed to distinguish hazard-depth intermediates from monetary damage
  surfaces).'
exposure:
  category: buildings, infrastructure, population
  dimension: population, structure
  quantity_kind: count
  taxonomy: GED4ALL
extra_attributions:
- email: clorillou@worldbank.org
  id: attribution_ttl
  name: Cecile Lorillou
  role: world_bank_team_lead
  url: https://www.worldbank.org
- email: https://capacity4dev.europa.eu/contact_en
  id: attribution_funder
  name: ACP-EU Natural Disaster Risk Reduction Program
  role: funder
  url: https://capacity4dev.europa.eu/groups/drr-acp/info/acp-eu-natural-disaster-risk-reduction-program_en
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic, probabilistic
  hazard_type: coastal_flood, flood, landslide
  intensity: wd:m
  occurrence_range: 'Erosion hazard lines/zones for baseline reference and future
    horizons (2040, 2070), including permanent (structural/SLR-related) and combined
    permanent+temporary storm erosion representations., Time horizons: 2020, 2040,
    2070; probability/return-period classes encoded in rasters: 0.4, 1, 10, 30, 100
    (as in filenames)., Time horizons: current (baseline), 2040, 2070; return periods
    encoded in rasters: T1, T4, T5, T10, T25, T100, T250 (some also provided as corrected
    variants).'
  processes: coastal_flood, landslide_general, pluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: 'Coastal flood loss outputs for Greater Banjul Area derived from coastal
    inundation ''flat'' sea-level scenarios combined with exposure and depth-damage
    functions. Inventory indicates coastal scenario rasters under 2020/2040/2070 with
    naming pattern: flat scenario_{waterlevel}m_{year}_{class}.tif (e.g., 0.4/1/10/30/100
    classes; water levels vary by horizon). Confirm whether stored rasters are monetary
    loss values (USD) or intermediate inundation depths; treat as economic loss layers
    per project methodology described in the PDFs., Risk / prioritization index rasters
    provided as corrected risk surfaces for Coastal, Urban, and Combined cases for
    2020/2040/2070 (e.g., Coastal_2020_risk_corrected.tif, Urban_2040_risk_corrected.tif,
    Combined_2070_risk_corrected.tif). Interpreted as a normalized damage/risk index
    (non-monetary). If these rasters actually represent expected annual loss (EAL/AAL)
    or other monetary risk metrics, re-map impact_metric to loss_annual_average_value
    and set quantity_kind=monetary with currency=USD., Urban flood loss outputs for
    Greater Banjul Area derived from probabilistic pluvial flood hazard modelling
    and depth-damage functions applied to building / land-use exposure. Inventory
    indicates urban return-period rasters with naming pattern: T{RP}_max_wd_{year}_corrected.tif
    (e.g., T1/T5/T10/T25/T100/T250 for current/2040/2070). Confirm whether values
    represent monetary losses (USD) or intermediate depth grids; treat as economic
    loss layers per project methodology described in the PDFs.'
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: coastal_flood, pluvial_flood
  hazard_type: coastal_flood, flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: The Gambia Integrated Urban and Coastal Resilience Program
  url: https://www.gfdrr.org/en/gambia-integrated-urban-and-coastal-resilience-technical-assistance-program
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support flood and coastal risk assessment and the prioritization of investment
  options for resilience in the Greater Banjul Area by providing spatial hazard, exposure,
  and risk/loss datasets for current conditions and future horizons.
resources:
- coordinate_system: null
  description: ArcGIS Map Journal web application providing an interactive narrative
    overview of the flood and coastal risk assessment for the Greater Banjul Area.
    Presents key findings, hazard maps, risk outputs, and investment planning recommendations
    through an interactive dashboard interface.
  download_url: https://geowb.maps.arcgis.com/apps/MapJournal/index.html?appid=a7884f06912c4e73a73c49a9feebda68#
  format: JSON (json)
  id: resource_storymap
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Interactive Story Map - Flood and Coastal Risk Assessment for Greater Banjul
- coordinate_system: EPSG:32628
  description: 'Zip archive containing vector exposure data for the Greater Banjul
    Area. Includes the File Geodatabase Landuse.gdb with four key layers: (1) LU_GBA_5_0
    - land use polygons with attribute Category (e.g., Residential, Shrubs, Forest,
    essential access routes); (2) Road_essential - lines with attribute eclass (e.g.,
    Essential access routes paved/unpaved); (3) Critical_facilities - polygons with
    building_name and Category (e.g., Hospital, School, Fire Station); (4) Critical_facilities_point
    - points with Category_2 and name_building. Also includes LU_GBA_5_0.zip packaging
    the land use polygon layer as a Shapefile set for GIS interoperability.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095906/01_Landuse.zip
  format: File Geodatabase (gdb)
  id: resource_landuse
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Land Use and Exposure Layers
- coordinate_system: EPSG:32628
  description: 'Zip archive containing 36 flood hazard GeoTIFF rasters for the Greater
    Banjul Area, organized into Coastal and Urban subfolders for time horizons 2020,
    2040, and 2070. Urban flood hazard (21 files): maximum water depth rasters following
    naming convention T{RP}_max_wd_{YEAR}.tif, where RP indicates return period category
    (T04, T1, T5, T10, T25, T100, T250) for each horizon (current/2020, 2040, 2070).
    Coastal flood hazard (15 files): flat scenario inundation rasters following naming
    convention flat scenario_{water_level}m_{YEAR}_{RP}.tif, where water_level is
    the total water level in meters and RP is the return period class (0.4, 1, 10,
    30, 100 years) for each horizon. Intensity measure: maximum water depth in meters.
    Coordinate system: WGS84 / UTM zone 28N (EPSG:32628).'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095907/02_Flood_Hazard.zip
  format: GeoTIFF (tif)
  id: resource_flood_hazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Flood Hazard Rasters - Coastal and Urban
- coordinate_system: EPSG:32628
  description: 'Zip archive containing an Esri File Geodatabase (Erosion hazard.gdb)
    with coastal erosion hazard vector layers for the Greater Banjul Area. Contains
    5 line feature layers: (1) Erosion_zone_2040_years_Permanent_erosion - permanent
    erosion zone projected to 2040; (2) Erosion_zone_2040_years_Permanent_erosion_Temporary_storm_erosion
    - combined permanent and temporary storm erosion zone for 2040; (3) Erosion_zone_2070_permanent
    - permanent erosion zone projected to 2070; (4) Erosion_zone_2070_years_Permanent_erosion_Temporary_storm_erosion
    - combined permanent and temporary storm erosion zone for 2070; (5) Reference_coastline_position_January_2020
    - baseline reference coastline.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095908/03_Erosion_Hazard.zip
  format: File Geodatabase (gdb)
  id: resource_erosion_hazard
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal Erosion Hazard Vectors
- coordinate_system: EPSG:32628
  description: Zip archive containing 9 risk output GeoTIFF rasters for the Greater
    Banjul Area, providing three risk surfaces (Coastal, Urban, Combined) for each
    time horizon 2020, 2040, and 2070. Files follow the naming convention {TYPE}_{YEAR}_risk_corrected.tif
    where TYPE is Coastal, Urban, or Combined. These are downstream products derived
    from the hazard-exposure-vulnerability workflow, integrating flood hazard depth
    with land use exposure and damage functions to produce spatially distributed risk
    estimates.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095909/04_Risk.zip
  format: GeoTIFF (tif)
  id: resource_risk
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Risk Output Rasters - Coastal, Urban, and Combined
- coordinate_system: EPSG:32628
  description: Zip archive containing 33 GeoTIFF rasters for the Greater Banjul Area,
    organized by Coastal and Urban subfolders for time horizons 2020, 2040, and 2070.
    Urban rasters (stored under Urban {YEAR} folders) follow naming convention T{RP}_max_wd_{YEAR}_corrected.tif,
    representing corrected maximum water depth surfaces per return period. Coastal
    rasters (stored under Coastal {YEAR} uncorrected folders) follow naming convention
    flat scenario_{water_level}m_{YEAR}_{RP}.tif, representing coastal inundation
    depth surfaces. These rasters serve as intermediate depth outputs used in conjunction
    with exposure and vulnerability data to compute the risk_corrected rasters in
    the Risk package.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095910/05_Damage.zip
  format: GeoTIFF (tif)
  id: resource_damage
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Damage Rasters - Coastal and Urban Flood Depth Outputs
- coordinate_system: EPSG:32628
  description: 'Zip archive containing an Esri File Geodatabase (Areas.gdb) with supporting
    polygon boundaries for the Greater Banjul Area study. Contains two polygon layers:
    (1) Areas - study/aggregation units used for hotspot reporting and summarization
    of risk results across the Greater Banjul Area (Banjul, Kanifing Municipality,
    Kombo North/Central/South); (2) Project_boundary - overall project boundary/extent
    delineating the geographic scope of the flood and coastal risk assessment.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095911/06_Areas.zip
  format: File Geodatabase (gdb)
  id: resource_areas
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Project Boundary and Study Areas
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_hevl-gmb_iucrp_floodcoastres
spatial:
  countries:
  - GMB
  gazetteer_entries:
  - description: Banjul
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/2413876/banjul.html
  - description: Kanifing
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/2413106/kanifing.html
  scale: sub-national
title: Flood and Coastal Risk Assessment and Priority Investment Planning for Greater
  Banjul Area, The Gambia
version: '1'
vulnerability:
  approach: hybrid
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: coastal_flood, flood
  hazard_process_primary: coastal_flood, pluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete
  taxonomy: Custom
  unit: ''
---
