#!/usr/bin/env python3
#this belongs in apps/methods/svg_icon_factory.py - Version: 6
# X-Seti - November26 2025 - Multi-Emulator Launcher - Complete SVG Icon Factory

"""
SVG Icon Factory - COMPLETE Version 6
ALL 22 SVG icons - theme aware with color parameter
No duplicate icon methods elsewhere in the project
"""

from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter, QIcon, QColor
from PyQt6.QtCore import Qt

##Methods list -
# chip_icon
# close_icon
# controller_icon
# file_icon
# folder_icon
# info_icon
# launch_icon
# manage_icon
# maximize_icon
# mel_app_icon
# minimize_icon
# package_icon
# paint_icon
# pause_icon
# properties_icon
# record_icon
# save_icon
# screenshot_icon
# settings_icon
# stop_icon
# volume_down_icon
# volume_up_icon
# _create_icon

##class SVGIconFactory -

class SVGIconFactory: #vers 6
    """Factory class for creating theme-aware SVG icons"""
    
    @staticmethod
    def _create_icon(svg_data: str, size: int = 20, color: str = None) -> QIcon: #vers 6
        """
        Create QIcon from SVG data with theme color support
        
        Args:
            svg_data: SVG string with 'currentColor' placeholders
            size: Icon size in pixels (default 20)
            color: Hex color for icon (e.g. '#ffffff', '#000000')
                   If None, uses currentColor (theme-aware)
        """
        if color:
            svg_data = svg_data.replace('currentColor', color)
        
        try:
            renderer = QSvgRenderer(svg_data.encode())
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            return QIcon(pixmap)
        except Exception as e:
            print(f"Error creating icon: {e}")
            return QIcon()
    

# - PLAYBACK CONTROL ICONS

    
    @staticmethod
    def launch_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Play/Launch icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor" d="M8 5v14l11-7z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def stop_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Stop icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <rect x="6" y="6" width="12" height="12" fill="currentColor"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def pause_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Pause icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <rect x="6" y="5" width="4" height="14" fill="currentColor"/>
            <rect x="14" y="5" width="4" height="14" fill="currentColor"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    

# - FILE & FOLDER ICONS

    
    @staticmethod
    def folder_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Folder icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M10,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V8C22,6.89 21.1,6 20,6H12L10,4Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def save_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Save/floppy icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M15,9H5V5H15M12,19A3,3 0 0,1 9,16A3,3 0 0,1 12,13A3,3 0 0,1 15,16A3,3 0 0,1 12,19M17,3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V7L17,3Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def file_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """File/document icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    

# - SETTINGS & CONFIGURATION ICONS

    @staticmethod
    def settings_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Settings gear icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8M12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12A2,2 0 0,0 12,10M10,22C9.75,22 9.54,21.82 9.5,21.58L9.13,18.93C8.5,18.68 7.96,18.34 7.44,17.94L4.95,18.95C4.73,19.03 4.46,18.95 4.34,18.73L2.34,15.27C2.21,15.05 2.27,14.78 2.46,14.63L4.57,12.97L4.5,12L4.57,11L2.46,9.37C2.27,9.22 2.21,8.95 2.34,8.73L4.34,5.27C4.46,5.05 4.73,4.96 4.95,5.05L7.44,6.05C7.96,5.66 8.5,5.32 9.13,5.07L9.5,2.42C9.54,2.18 9.75,2 10,2H14C14.25,2 14.46,2.18 14.5,2.42L14.87,5.07C15.5,5.32 16.04,5.66 16.56,6.05L19.05,5.05C19.27,4.96 19.54,5.05 19.66,5.27L21.66,8.73C21.79,8.95 21.73,9.22 21.54,9.37L19.43,11L19.5,12L19.43,13L21.54,14.63C21.73,14.78 21.79,15.05 21.66,15.27L19.66,18.73C19.54,18.95 19.27,19.04 19.05,18.95L16.56,17.95C16.04,18.34 15.5,18.68 14.87,18.93L14.5,21.58C14.46,21.82 14.25,22 14,22H10M11.25,4L10.88,6.61C9.68,6.86 8.62,7.5 7.85,8.39L5.44,7.35L4.69,8.65L6.8,10.2C6.4,11.37 6.4,12.64 6.8,13.8L4.68,15.36L5.43,16.66L7.86,15.62C8.63,16.5 9.68,17.14 10.87,17.38L11.24,20H12.76L13.13,17.39C14.32,17.14 15.37,16.5 16.14,15.62L18.57,16.66L19.32,15.36L17.2,13.81C17.6,12.64 17.6,11.37 17.2,10.2L19.31,8.65L18.56,7.35L16.15,8.39C15.38,7.5 14.32,6.86 13.12,6.62L12.75,4H11.25Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def properties_icon(size: int = 24, color: str = None) -> QIcon: #vers 1
        """Properties/theme icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def controller_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Game controller icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M6,9H8V11H10V13H8V15H6V13H4V11H6V9M18.5,9A1.5,1.5 0 0,1 20,10.5A1.5,1.5 0 0,1 18.5,12A1.5,1.5 0 0,1 17,10.5A1.5,1.5 0 0,1 18.5,9M15.5,12A1.5,1.5 0 0,1 17,13.5A1.5,1.5 0 0,1 15.5,15A1.5,1.5 0 0,1 14,13.5A1.5,1.5 0 0,1 15.5,12M17,5A7,7 0 0,1 24,12A7,7 0 0,1 17,19C15.04,19 13.27,18.2 12,16.9C10.73,18.2 8.96,19 7,19A7,7 0 0,1 0,12A7,7 0 0,1 7,5H17Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def chip_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Microchip/BIOS icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M6,4H18V5H21V7H18V9H21V11H18V13H21V15H18V17H21V19H18V20H6V19H3V17H6V15H3V13H6V11H3V9H6V7H3V5H6V4M11,15V18H13V15H11M15,15V18H17V15H15M7,15V18H9V15H7M7,6V9H9V6H7M7,10V13H9V10H7M11,10V13H13V10H11M15,10V13H17V10H15M11,6V9H13V6H11M15,6V9H17V6H15Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    

    # WINDOW CONTROL ICONS

    
    @staticmethod
    def info_icon(size: int = 24, color: str = None) -> QIcon: #vers 6
        """Info icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M12 16v-4M12 8h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def minimize_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Minimize icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <line x1="5" y1="12" x2="19" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def maximize_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Maximize icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <rect x="5" y="5" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" rx="2"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def close_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Close icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <line x1="6" y1="6" x2="18" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <line x1="18" y1="6" x2="6" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    

    # MEDIA CONTROLS

    
    @staticmethod
    def volume_up_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Volume up icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M14,3.23V5.29C16.89,6.15 19,8.83 19,12C19,15.17 16.89,17.84 14,18.7V20.77C18,19.86 21,16.28 21,12C21,7.72 18,4.14 14,3.23M16.5,12C16.5,10.23 15.5,8.71 14,7.97V16C15.5,15.29 16.5,13.76 16.5,12M3,9V15H7L12,20V4L7,9H3Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def volume_down_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Volume down icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M5,9V15H9L14,20V4L9,9M18.5,12C18.5,10.23 17.5,8.71 16,7.97V16C17.5,15.29 18.5,13.76 18.5,12Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def screenshot_icon(size: int = 20, color: str = None) -> QIcon: #vers 6
        """Screenshot/camera icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M4,4H7L9,2H15L17,4H20A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4A2,2 0 0,1 2,18V6A2,2 0 0,1 4,4M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def record_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Record icon - always red, ignores color parameter"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="8" fill="#FF3333"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, None)  # Force no color
    

# - ART & MANAGEMENT ICONS

    
    @staticmethod
    def search_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Search/detect/magnifying glass icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)

    @staticmethod
    def database_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Database icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M12,3C7.58,3 4,4.79 4,7C4,9.21 7.58,11 12,11C16.42,11 20,9.21 20,7C20,4.79 16.42,3 12,3M4,9V12C4,14.21 7.58,16 12,16C16.42,16 20,14.21 20,12V9C20,11.21 16.42,13 12,13C7.58,13 4,11.21 4,9M4,14V17C4,19.21 7.58,21 12,21C16.42,21 20,19.21 20,17V14C20,16.21 16.42,18 12,18C7.58,18 4,16.21 4,14Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def paint_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Paint brush icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M20.71,4.63L19.37,3.29C19,2.9 18.35,2.9 17.96,3.29L9,12.25L11.75,15L20.71,6.04C21.1,5.65 21.1,5 20.71,4.63M7,14A3,3 0 0,0 4,17C4,18.31 2.84,19 2,19C2.92,20.22 4.5,21 6,21A4,4 0 0,0 10,17A3,3 0 0,0 7,14Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def manage_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Settings/manage icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)
    
    @staticmethod
    def package_icon(size: int = 20, color: str = None) -> QIcon: #vers 1
        """Package/box icon"""
        svg_data = '''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L6.04,7.5L12,10.85L17.96,7.5L12,4.15M5,15.91L11,19.29V12.58L5,9.21V15.91M19,15.91V9.21L13,12.58V19.29L19,15.91Z"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, color)


    def create_backface_icon(self): #vers 1
        """Backface culling toggle icon"""
        svg_data = b'''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 4 L20 8 L16 16 L8 16 L4 8 Z"
                fill="currentColor" opacity="0.8"/>
            <path d="M12 4 L8 16 M12 4 L16 16"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-dasharray="2,2"
                opacity="0.3"
                fill="none"/>
            <path d="M4 8 L12 4 L20 8 L16 16 L8 16 Z"
                stroke="currentColor"
                stroke-width="1.5"
                fill="none"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


# - APP ICON
    
    @staticmethod
    def mel_app_icon(size: int = 64) -> QIcon: #vers 1
        """MEL App Icon - Multi-Emulator Launcher with gradient"""
        svg_data = f'''<svg width="{size}" height="{size}" viewBox="0 0 64 64">
            <rect width="64" height="64" rx="12" fill="url(#grad1)"/>
            <defs>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#4A90E2;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#7B68EE;stop-opacity:1" />
                </linearGradient>
            </defs>
            <g transform="translate(8, 8)">
                <rect x="4" y="0" width="4" height="12" fill="#ffffff" opacity="0.3"/>
                <rect x="0" y="4" width="12" height="4" fill="#ffffff" opacity="0.3"/>
            </g>
            <circle cx="52" cy="12" r="2.5" fill="#ffffff" opacity="0.3"/>
            <circle cx="56" cy="16" r="2.5" fill="#ffffff" opacity="0.3"/>
            <text x="32" y="40" font-family="Arial, sans-serif" font-size="22" 
                  font-weight="bold" fill="#ffffff" text-anchor="middle">MEL</text>
            <text x="32" y="52" font-family="Arial, sans-serif" font-size="7" 
                  fill="#ffffff" opacity="0.8" text-anchor="middle">EMULATOR</text>
            <rect x="24" y="56" width="16" height="6" rx="1" fill="#ffffff" opacity="0.3"/>
        </svg>'''
        return SVGIconFactory._create_icon(svg_data, size, None)

#- Moved from Col_Workshop
    def _create_bitdepth_icon(self): #vers 3
        """Create bit depth icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M3,5H9V11H3V5M5,7V9H7V7H5M11,7H21V9H11V7M11,15H21V17H11V15M5,20L1.5,16.5L2.91,15.09L5,17.17L9.59,12.59L11,14L5,20Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_resize_icon(self): #vers 2
        """Create resize icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M10,21V19H6.41L10.91,14.5L9.5,13.09L5,17.59V14H3V21H10M14.5,10.91L19,6.41V10H21V3H14V5H17.59L13.09,9.5L14.5,10.91Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_warning_icon_svg(self): #vers 1
        """Create SVG warning icon for table display"""
        svg_data = b"""
        <svg width="16" height="16" viewBox="0 0 16 16">
            <path fill="#FFA500" d="M8 1l7 13H1z"/>
            <text x="8" y="12" font-size="10" fill="black" text-anchor="middle">!</text>
        </svg>
        """
        return QIcon(QPixmap.fromImage(
            QImage.fromData(QByteArray(svg_data))
        ))


    def _create_resize_icon2(self): #vers 1
        """Resize grip icon - diagonal arrows"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 6l-8 8M10 6h4v4M6 14v-4h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_upscale_icon(self): #vers 3
        """Create AI upscale icon - brain/intelligence style"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <!-- Brain outline -->
            <path d="M12 3 C8 3 5 6 5 9 C5 10 5.5 11 6 12 C5.5 13 5 14 5 15 C5 18 8 21 12 21 C16 21 19 18 19 15 C19 14 18.5 13 18 12 C18.5 11 19 10 19 9 C19 6 16 3 12 3 Z"
                fill="none" stroke="currentColor" stroke-width="1.5"/>

            <!-- Neural pathways inside -->
            <path d="M9 8 L10 10 M14 8 L13 10 M10 12 L14 12 M9 14 L12 16 M15 14 L12 16"
                stroke="currentColor" stroke-width="1" fill="none"/>

            <!-- Upward indicator -->
            <path d="M19 8 L19 4 M17 6 L19 4 L21 6"
                stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_upscale_icon(self): #vers 3
        """Create AI upscale icon - sparkle/magic AI style"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <!-- Large sparkle -->
            <path d="M12 2 L13 8 L12 14 L11 8 Z M8 12 L2 11 L8 10 L14 11 Z"
                fill="currentColor"/>

            <!-- Small sparkles -->
            <circle cx="18" cy="6" r="1.5" fill="currentColor"/>
            <circle cx="6" cy="18" r="1.5" fill="currentColor"/>
            <circle cx="19" cy="16" r="1" fill="currentColor"/>

            <!-- Upward arrow -->
            <path d="M16 20 L20 20 M18 18 L18 22"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_upscale_icon(self): #vers 3
        """Create AI upscale icon - neural network style"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <!-- Neural network nodes -->
            <circle cx="6" cy="6" r="2" fill="currentColor"/>
            <circle cx="18" cy="6" r="2" fill="currentColor"/>
            <circle cx="6" cy="18" r="2" fill="currentColor"/>
            <circle cx="18" cy="18" r="2" fill="currentColor"/>
            <circle cx="12" cy="12" r="2.5" fill="currentColor"/>

            <!-- Connecting lines -->
            <path d="M7.5 7.5 L10.5 10.5 M13.5 10.5 L16.5 7.5 M7.5 16.5 L10.5 13.5 M13.5 13.5 L16.5 16.5"
                stroke="currentColor" stroke-width="1.5" fill="none"/>

            <!-- Upward arrow overlay -->
            <path d="M12 3 L12 9 M9 6 L12 3 L15 6"
                stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_manage_icon(self): #vers 1
        """Create manage/settings icon for bumpmap manager"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <!-- Gear/cog icon for management -->
            <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_paint_icon(self): #vers 1
        """Create paint brush icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M20.71 7.04c.39-.39.39-1.04 0-1.41l-2.34-2.34c-.37-.39-1.02-.39-1.41 0l-1.84 1.83 3.75 3.75M3 17.25V21h3.75L17.81 9.93l-3.75-3.75L3 17.25z"
                fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_compress_icon(self): #vers 2
        """Create compress icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M4,2H20V4H13V10H20V12H4V10H11V4H4V2M4,13H20V15H13V21H20V23H4V21H11V15H4V13Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_backface_icon(self): #vers 1
        """Backface culling toggle - polygon with front/back sides"""
        svg_data = b'''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <!-- Front face (visible - solid) -->
            <path d="M12 4 L20 8 L16 16 L8 16 L4 8 Z"
                fill="currentColor" opacity="0.8"/>

            <!-- Back edge (hidden - dashed) -->
            <path d="M12 4 L8 16 M12 4 L16 16"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-dasharray="2,2"
                opacity="0.3"
                fill="none"/>

            <!-- Front edges (visible - solid) -->
            <path d="M4 8 L12 4 L20 8 L16 16 L8 16 Z"
                stroke="currentColor"
                stroke-width="1.5"
                fill="none"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_build_icon(self): #vers 1
        """Create build/construct icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M22,9 L12,2 L2,9 L12,16 L22,9 Z M12,18 L4,13 L4,19 L12,24 L20,19 L20,13 L12,18 Z"
                fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_uncompress_icon(self): #vers 2
        """Create uncompress icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor" d="M11,4V2H13V4H11M13,21V19H11V21H13M4,12V10H20V12H4Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_view_icon(self): #vers 2
        """Create view/eye icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor"
                d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9
                    M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17
                    M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5
                    C17,19.5 21.27,16.39 23,12
                    C21.27,7.61 17,4.5 12,4.5Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_add_icon(self): #vers 2
        """Create add/plus icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor" d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_delete_icon(self): #vers 2
        """Create delete/minus icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path fill="currentColor" d="M19,13H5V11H19V13Z"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_color_picker_icon(self): #vers 1
        """Color picker icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="2"/>
            <path d="M10 3v4M10 13v4M3 10h4M13 10h4" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_zoom_in_icon(self): #vers 1
        """Zoom in icon (+)"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2"/>
            <path d="M8 5v6M5 8h6" stroke="currentColor" stroke-width="2"/>
            <path d="M13 13l4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_zoom_out_icon(self): #vers 1
        """Zoom out icon (-)"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2"/>
            <path d="M5 8h6" stroke="currentColor" stroke-width="2"/>
            <path d="M13 13l4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_reset_icon(self): #vers 1
        """Reset/1:1 icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 10A6 6 0 1 1 4 10M4 10l3-3m-3 3l3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_fit_icon(self): #vers 1
        """Fit to window icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3" y="3" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M7 7l6 6M13 7l-6 6" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_arrow_up_icon(self): #vers 1
        """Arrow up"""
        svg_data = b'''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 3v10M4 7l4-4 4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=16)


    def _create_arrow_down_icon(self): #vers 1
        """Arrow down"""
        svg_data = b'''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 13V3M12 9l-4 4-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=16)


    def _create_arrow_left_icon(self): #vers 1
        """Arrow left"""
        svg_data = b'''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 8h10M7 4L3 8l4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=16)


    def _create_arrow_right_icon(self): #vers 1
        """Arrow right"""
        svg_data = b'''<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M13 8H3M9 12l4-4-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=16)


    def _create_flip_vert_icon(self): #vers 1
        """Create vertical flip SVG icon"""
        from PyQt6.QtGui import QIcon, QPixmap, QPainter
        from PyQt6.QtSvg import QSvgRenderer

        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12h18M8 7l-4 5 4 5M16 7l4 5-4 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_flip_horz_icon(self): #vers 1
        """Create horizontal flip SVG icon"""
        from PyQt6.QtGui import QIcon, QPixmap, QPainter
        from PyQt6.QtSvg import QSvgRenderer

        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 3v18M7 8l5-4 5 4M7 16l5 4 5-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_rotate_cw_icon(self): #vers 1
        """Create clockwise rotation SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 12a9 9 0 11-9-9v6M21 3l-3 6-6-3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_rotate_ccw_icon(self): #vers 1
        """Create counter-clockwise rotation SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12a9 9 0 109-9v6M3 3l3 6 6-3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_copy_icon(self): #vers 1
        """Create copy SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="9" y="9" width="13" height="13" rx="2" stroke="currentColor" stroke-width="2"/>
            <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1" stroke="currentColor" stroke-width="2"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_paste_icon(self): #vers 1
        """Create paste SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2" stroke="currentColor" stroke-width="2"/>
            <rect x="8" y="2" width="8" height="4" rx="1" stroke="currentColor" stroke-width="2"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_edit_icon(self): #vers 1
        """Create edit SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7" stroke="currentColor" stroke-width="2"/>
            <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_convert_icon(self): #vers 1
        """Create convert SVG icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12h18M3 12l4-4M3 12l4 4M21 12l-4-4M21 12l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/>
        </svg>'''

        return self._svg_to_icon(svg_data)


    def _create_undo_icon(self): #vers 2
        """Undo - Curved arrow icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M3 7v6h6M3 13a9 9 0 1018 0 9 9 0 00-18 0z"
                stroke="currentColor" stroke-width="2" fill="none"
                stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_info_icon(self): #vers 1
        """Info - circle with 'i' icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/>
            <path d="M12 11v6M12 8v.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_folder_icon(self): #vers 1
        """Open IMG - Folder icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-7l-2-2H5a2 2 0 00-2 2z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_file_icon(self): #vers 1
        """Open col - File icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z" stroke="currentColor" stroke-width="2"/>
            <path d="M14 2v6h6" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_open_icon(self): #vers 1
        """Open - Folder icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M3 7v13a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_save_icon(self): #vers 1
        """Save col - Floppy disk icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z" stroke="currentColor" stroke-width="2"/>
            <path d="M17 21v-8H7v8M7 3v5h8" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_import_icon(self): #vers 1
        """Import - Download/Import icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_export_icon(self): #vers 1
        """Export - Upload/Export icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_saveas_icon(self): #vers 1
        """Save - Floppy disk icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="17 21 17 13 7 13 7 21"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="7 3 7 8 15 8"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_analyze_icon(self): #vers 1
        """Analyze - Bar chart icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <line x1="18" y1="20" x2="18" y2="10"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <line x1="12" y1="20" x2="12" y2="4"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <line x1="6" y1="20" x2="6" y2="14"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_sphere_icon(self): #vers 1
        """Sphere - Circle icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10"
                stroke="currentColor" stroke-width="2"
                fill="none"/>
            <path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"
                stroke="currentColor" stroke-width="2"
                fill="none"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_box_icon(self): #vers 1
        """Box - Cube icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="3.27 6.96 12 12.01 20.73 6.96"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="12" y1="22.08" x2="12" y2="12"
                stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_mesh_icon(self): #vers 1
        """Mesh - Grid/wireframe icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <rect x="3" y="3" width="18" height="18"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="3" y1="9" x2="21" y2="9"
                stroke="currentColor" stroke-width="2"/>
            <line x1="3" y1="15" x2="21" y2="15"
                stroke="currentColor" stroke-width="2"/>
            <line x1="9" y1="3" x2="9" y2="21"
                stroke="currentColor" stroke-width="2"/>
            <line x1="15" y1="3" x2="15" y2="21"
                stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_package_icon(self): #vers 1
        """Export All - Package/Box icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="2"/>
            <path d="M3.27 6.96L12 12.01l8.73-5.05M12 22.08V12" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_properties_icon(self): #vers 1
        """Properties - Info/Details icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <path d="M12 16v-4M12 8h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    # CONTEXT MENU ICONS

    def _create_plus_icon(self): #vers 1
        """Create New Entry - Plus icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <path d="M12 8v8M8 12h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_document_icon(self): #vers 1
        """Create New col - Document icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z" stroke="currentColor" stroke-width="2"/>
            <path d="M14 2v6h6M16 13H8M16 17H8M10 9H8" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_filter_icon(self): #vers 1
        """Filter/sliders icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="6" cy="4" r="2" fill="currentColor"/>
            <rect x="5" y="8" width="2" height="8" fill="currentColor"/>
            <circle cx="14" cy="12" r="2" fill="currentColor"/>
            <rect x="13" y="4" width="2" height="6" fill="currentColor"/>
            <circle cx="10" cy="8" r="2" fill="currentColor"/>
            <rect x="9" y="12" width="2" height="4" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_add_icon(self): #vers 1
        """Add/plus icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_trash_icon(self): #vers 1
        """Delete/trash icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 5h14M8 5V3h4v2M6 5v11a1 1 0 001 1h6a1 1 0 001-1V5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_filter_icon(self): #vers 1
        """Filter/sliders icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="6" cy="4" r="2" fill="currentColor"/>
            <rect x="5" y="8" width="2" height="8" fill="currentColor"/>
            <circle cx="14" cy="12" r="2" fill="currentColor"/>
            <rect x="13" y="4" width="2" height="6" fill="currentColor"/>
            <circle cx="10" cy="8" r="2" fill="currentColor"/>
            <rect x="9" y="12" width="2" height="4" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_delete_icon(self): #vers 1
        """Delete/trash icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 5h14M8 5V3h4v2M6 5v11a1 1 0 001 1h6a1 1 0 001-1V5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_duplicate_icon(self): #vers 1
        """Duplicate/copy icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="6" y="6" width="10" height="10" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M4 4h8v2H6v8H4V4z" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_create_icon(self): #vers 1
        """Create/new icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10 4v12M4 10h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_filter_icon(self): #vers 1
        """Filter/sliders icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="6" cy="4" r="2" fill="currentColor"/>
            <rect x="5" y="8" width="2" height="8" fill="currentColor"/>
            <circle cx="14" cy="12" r="2" fill="currentColor"/>
            <rect x="13" y="4" width="2" height="6" fill="currentColor"/>
            <circle cx="10" cy="8" r="2" fill="currentColor"/>
            <rect x="9" y="12" width="2" height="4" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_pencil_icon(self): #vers 1
        """Edit - Pencil icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 3a2.83 2.83 0 114 4L7.5 20.5 2 22l1.5-5.5L17 3z" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_trash_icon(self): #vers 1
        """Delete - Trash icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6M8 6V4a2 2 0 012-2h4a2 2 0 012 2v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_check_icon(self): #vers 2
        """Create check/verify icon - document with checkmark"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z"
                fill="none" stroke="currentColor" stroke-width="2"/>
            <path d="M14 2v6h6"
                stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M9 13l2 2 4-4"
                stroke="currentColor" stroke-width="2" fill="none"
                stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_eye_icon(self): #vers 1
        """View - Eye icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" stroke="currentColor" stroke-width="2"/>
            <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_list_icon(self): #vers 1
        """Properties List - List icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    # WINDOW CONTROL ICONS

    def _create_minimize_icon(self): #vers 1
        """Minimize - Horizontal line"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_maximize_icon(self): #vers 1
        """Maximize - Square"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" strokea-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_close_icon(self): #vers 1
        """Close - X icon"""
        svg_data = b'''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data)


    def _create_settings_icon(self): #vers 1
        """Settings/gear icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="3" stroke="currentColor" stroke-width="2"/>
            <path d="M10 2v2M10 16v2M2 10h2M16 10h2M4.93 4.93l1.41 1.41M13.66 13.66l1.41 1.41M4.93 15.07l1.41-1.41M13.66 6.34l1.41-1.41" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_minimize_icon(self): #vers 1
        """Minimize - Horizontal line icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <line x1="5" y1="12" x2="19" y2="12"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_maximize_icon(self): #vers 1
        """Maximize - Square icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <rect x="5" y="5" width="14" height="14"
                stroke="currentColor" stroke-width="2"
                fill="none" rx="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_close_icon(self): #vers 1
        """Close - X icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <line x1="6" y1="6" x2="18" y2="18"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
            <line x1="18" y1="6" x2="6" y2="18"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_add_icon(self): #vers 1
        """Add - Plus icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <line x1="12" y1="5" x2="12" y2="19"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
            <line x1="5" y1="12" x2="19" y2="12"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_delete_icon(self): #vers 1
        """Delete - Trash icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <polyline points="3 6 5 6 21 6"
                    stroke="currentColor" stroke-width="2"
                    fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_import_icon(self): #vers 1
        """Import - Download arrow icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="7 10 12 15 17 10"
                    stroke="currentColor" stroke-width="2"
                    fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="12" y1="15" x2="12" y2="3"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_export_icon(self): #vers 1
        """Export - Upload arrow icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"
                stroke="currentColor" stroke-width="2"
                fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <polyline points="17 8 12 3 7 8"
                    stroke="currentColor" stroke-width="2"
                    fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="12" y1="3" x2="12" y2="15"
                stroke="currentColor" stroke-width="2"
                stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_checkerboard_icon(self): #vers 1
        """Create checkerboard pattern icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="0" y="0" width="5" height="5" fill="currentColor"/>
            <rect x="5" y="5" width="5" height="5" fill="currentColor"/>
            <rect x="10" y="0" width="5" height="5" fill="currentColor"/>
            <rect x="15" y="5" width="5" height="5" fill="currentColor"/>
            <rect x="0" y="10" width="5" height="5" fill="currentColor"/>
            <rect x="5" y="15" width="5" height="5" fill="currentColor"/>
            <rect x="10" y="10" width="5" height="5" fill="currentColor"/>
            <rect x="15" y="15" width="5" height="5" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_undo_icon(self): #vers 2
        """Undo - Curved arrow icon"""
        svg_data = b'''<svg viewBox="0 0 24 24">
            <path d="M3 7v6h6M3 13a9 9 0 1018 0 9 9 0 00-18 0z"
                stroke="currentColor" stroke-width="2" fill="none"
                stroke-linecap="round" stroke-linejoin="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_sphere_icon(self): #vers 1
        """Sphere collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="2" fill="none"/>
            <ellipse cx="10" cy="10" rx="7" ry="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
            <path d="M3 10 Q10 13 17 10" stroke="currentColor" stroke-width="1.5" fill="none"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_box_icon(self): #vers 1
        """Box collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 6 L10 3 L16 6 L16 14 L10 17 L4 14 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M4 6 L10 9 L16 6" stroke="currentColor" stroke-width="2"/>
            <path d="M10 9 L10 17" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_mesh_icon(self): #vers 1
        """Mesh collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 10 L10 3 L17 10 L10 17 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M3 10 L17 10 M10 3 L10 17" stroke="currentColor" stroke-width="1.5"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_wireframe_icon(self): #vers 1
        """Wireframe mode icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 5 L15 5 L15 15 L5 15 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M5 10 L15 10 M10 5 L10 15" stroke="currentColor" stroke-width="1.5"/>
            <circle cx="5" cy="5" r="1.5" fill="currentColor"/>
            <circle cx="15" cy="5" r="1.5" fill="currentColor"/>
            <circle cx="15" cy="15" r="1.5" fill="currentColor"/>
            <circle cx="5" cy="15" r="1.5" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_bounds_icon(self): #vers 1
        """Bounding box icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3" y="3" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
            <path d="M3 3 L7 3 M17 3 L13 3 M3 17 L7 17 M17 17 L13 17 M3 3 L3 7 M3 17 L3 13 M17 3 L17 7 M17 17 L17 13" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_reset_view_icon(self): #vers 1
        """Reset camera view icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 10A6 6 0 1 1 4 10M4 10l3-3m-3 3l3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_sphere_icon(self): #vers 1
        """Sphere collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="2" fill="none"/>
            <ellipse cx="10" cy="10" rx="7" ry="3" stroke="currentColor" stroke-width="1.5" fill="none"/>
            <path d="M3 10 Q10 13 17 10" stroke="currentColor" stroke-width="1.5" fill="none"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_box_icon(self): #vers 1
        """Box collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 6 L10 3 L16 6 L16 14 L10 17 L4 14 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M4 6 L10 9 L16 6" stroke="currentColor" stroke-width="2"/>
            <path d="M10 9 L10 17" stroke="currentColor" stroke-width="2"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_mesh_icon(self): #vers 1
        """Mesh collision icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 10 L10 3 L17 10 L10 17 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M3 10 L17 10 M10 3 L10 17" stroke="currentColor" stroke-width="1.5"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_wireframe_icon(self): #vers 1
        """Wireframe mode icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 5 L15 5 L15 15 L5 15 Z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M5 10 L15 10 M10 5 L10 15" stroke="currentColor" stroke-width="1.5"/>
            <circle cx="5" cy="5" r="1.5" fill="currentColor"/>
            <circle cx="15" cy="5" r="1.5" fill="currentColor"/>
            <circle cx="15" cy="15" r="1.5" fill="currentColor"/>
            <circle cx="5" cy="15" r="1.5" fill="currentColor"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_bounds_icon(self): #vers 1
        """Bounding box icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="3" y="3" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
            <path d="M3 3 L7 3 M17 3 L13 3 M3 17 L7 17 M17 17 L13 17 M3 3 L3 7 M3 17 L3 13 M17 3 L17 7 M17 17 L17 13" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)


    def _create_reset_view_icon(self): #vers 1
        """Reset camera view icon"""
        svg_data = b'''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 10A6 6 0 1 1 4 10M4 10l3-3m-3 3l3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>'''
        return self._svg_to_icon(svg_data, size=20)



    def _svg_to_icon(self, svg_data, size=24): #vers 2
        """Convert SVG data to QIcon with theme color support"""
        from PyQt6.QtGui import QIcon, QPixmap, QPainter, QColor
        from PyQt6.QtSvg import QSvgRenderer
        from PyQt6.QtCore import QByteArray

        try:
            # Get current text color from palette
            text_color = self.palette().color(self.foregroundRole())

            # Replace currentColor with actual color
            svg_str = svg_data.decode('utf-8')
            svg_str = svg_str.replace('currentColor', text_color.name())
            svg_data = svg_str.encode('utf-8')

            renderer = QSvgRenderer(QByteArray(svg_data))
            pixmap = QPixmap(size, size)
            pixmap.fill(QColor(0, 0, 0, 0))  # Transparent background

            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()

            return QIcon(pixmap)
        except:
            # Fallback to no icon if SVG fails
            return QIcon()



# CLI testing
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QScrollArea
    import sys
    
    app = QApplication(sys.argv)
    
    window = QWidget()
    window.setWindowTitle("SVG Icon Factory v6 - ALL 22 Icons")
    main_layout = QHBoxLayout(window)
    
    # Dark theme column
    dark_scroll = QScrollArea()
    dark_scroll.setWidgetResizable(True)
    dark_col = QWidget()
    dark_col.setStyleSheet("background: #2b2b2b; color: #ffffff;")
    dark_layout = QVBoxLayout(dark_col)
    dark_title = QLabel("Dark Theme (White Icons)")
    dark_title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 10px;")
    dark_layout.addWidget(dark_title)
    
    dark_icons = [
        ("Launch", SVGIconFactory.launch_icon(20, "#ffffff")),
        ("Stop", SVGIconFactory.stop_icon(20, "#ffffff")),
        ("Pause", SVGIconFactory.pause_icon(20, "#ffffff")),
        ("Folder", SVGIconFactory.folder_icon(20, "#ffffff")),
        ("Save", SVGIconFactory.save_icon(20, "#ffffff")),
        ("File", SVGIconFactory.file_icon(20, "#ffffff")),
        ("Settings", SVGIconFactory.settings_icon(20, "#ffffff")),
        ("Properties", SVGIconFactory.properties_icon(24, "#ffffff")),
        ("Controller", SVGIconFactory.controller_icon(20, "#ffffff")),
        ("Chip/BIOS", SVGIconFactory.chip_icon(20, "#ffffff")),
        ("Info", SVGIconFactory.info_icon(24, "#ffffff")),
        ("Minimize", SVGIconFactory.minimize_icon(20, "#ffffff")),
        ("Maximize", SVGIconFactory.maximize_icon(20, "#ffffff")),
        ("Close", SVGIconFactory.close_icon(20, "#ffffff")),
        ("Volume Up", SVGIconFactory.volume_up_icon(20, "#ffffff")),
        ("Volume Down", SVGIconFactory.volume_down_icon(20, "#ffffff")),
        ("Screenshot", SVGIconFactory.screenshot_icon(20, "#ffffff")),
        ("Record", SVGIconFactory.record_icon(20)),
        ("Paint", SVGIconFactory.paint_icon(20, "#ffffff")),
        ("Manage", SVGIconFactory.manage_icon(20, "#ffffff")),
        ("Package", SVGIconFactory.package_icon(20, "#ffffff")),
        ("MEL App", SVGIconFactory.mel_app_icon(48)),
    ]
    
    for name, icon in dark_icons:
        btn = QPushButton(name)
        btn.setIcon(icon)
        btn.setIconSize(Qt.QSize(20, 20))
        btn.setStyleSheet("padding: 6px; text-align: left; background: #3c3c3c; border: 1px solid #555;")
        dark_layout.addWidget(btn)
    
    dark_scroll.setWidget(dark_col)
    
    # Light theme column
    light_scroll = QScrollArea()
    light_scroll.setWidgetResizable(True)
    light_col = QWidget()
    light_col.setStyleSheet("background: #ffffff; color: #000000;")
    light_layout = QVBoxLayout(light_col)
    light_title = QLabel("Light Theme (Black Icons)")
    light_title.setStyleSheet("font-weight: bold; font-size: 14px; padding: 10px;")
    light_layout.addWidget(light_title)
    
    light_icons = [
        ("Launch", SVGIconFactory.launch_icon(20, "#000000")),
        ("Stop", SVGIconFactory.stop_icon(20, "#000000")),
        ("Pause", SVGIconFactory.pause_icon(20, "#000000")),
        ("Folder", SVGIconFactory.folder_icon(20, "#000000")),
        ("Save", SVGIconFactory.save_icon(20, "#000000")),
        ("File", SVGIconFactory.file_icon(20, "#000000")),
        ("Settings", SVGIconFactory.settings_icon(20, "#000000")),
        ("Properties", SVGIconFactory.properties_icon(24, "#000000")),
        ("Controller", SVGIconFactory.controller_icon(20, "#000000")),
        ("Chip/BIOS", SVGIconFactory.chip_icon(20, "#000000")),
        ("Info", SVGIconFactory.info_icon(24, "#000000")),
        ("Minimize", SVGIconFactory.minimize_icon(20, "#000000")),
        ("Maximize", SVGIconFactory.maximize_icon(20, "#000000")),
        ("Close", SVGIconFactory.close_icon(20, "#000000")),
        ("Volume Up", SVGIconFactory.volume_up_icon(20, "#000000")),
        ("Volume Down", SVGIconFactory.volume_down_icon(20, "#000000")),
        ("Screenshot", SVGIconFactory.screenshot_icon(20, "#000000")),
        ("Record", SVGIconFactory.record_icon(20)),
        ("Paint", SVGIconFactory.paint_icon(20, "#000000")),
        ("Manage", SVGIconFactory.manage_icon(20, "#000000")),
        ("Package", SVGIconFactory.package_icon(20, "#000000")),
        ("MEL App", SVGIconFactory.mel_app_icon(48)),
    ]
    
    for name, icon in light_icons:
        btn = QPushButton(name)
        btn.setIcon(icon)
        btn.setIconSize(Qt.QSize(20, 20))
        btn.setStyleSheet("padding: 6px; text-align: left; background: #f0f0f0; border: 1px solid #ccc;")
        light_layout.addWidget(btn)
    
    light_scroll.setWidget(light_col)
    
    main_layout.addWidget(dark_scroll)
    main_layout.addWidget(light_scroll)
    
    window.setGeometry(100, 100, 700, 800)
    window.show()
    
    print("\n✓ SVG Icon Factory v6 - Complete with ALL 22 Icons")
    print("  Playback: launch, stop, pause")
    print("  Files: folder, save, file")
    print("  Settings: settings, properties, controller, chip")
    print("  Window: info, minimize, maximize, close")
    print("  Media: volume_up, volume_down, screenshot, record")
    print("  Art: paint, manage, package")
    print("  App: mel_app_icon")
    
    sys.exit(app.exec())
